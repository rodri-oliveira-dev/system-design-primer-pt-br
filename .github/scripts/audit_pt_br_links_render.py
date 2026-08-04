from __future__ import annotations

import concurrent.futures
import os
import re
import sys
import time
import urllib.parse
from collections import Counter
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

FILES = [Path("README-pt-BR.md"), Path("CONTRIBUTING-pt-BR.md"), Path("CONTRIBUTING.md")]
USER_AGENT = "system-design-primer-pt-br-link-audit/1.1"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPOSITORY = os.environ["GITHUB_REPOSITORY"]

md = MarkdownIt("commonmark", {"html": True})


def walk(tokens):
    for token in tokens:
        yield token
        if token.children:
            yield from walk(token.children)


def extract_destinations(text: str) -> tuple[list[str], list[str]]:
    links: list[str] = []
    images: list[str] = []

    for token in walk(md.parse(text)):
        if token.type == "link_open":
            href = token.attrGet("href")
            if href:
                links.append(href)
        elif token.type == "image":
            src = token.attrGet("src")
            if src:
                images.append(src)

    links.extend(re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', text, flags=re.I))
    images.extend(re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', text, flags=re.I))
    return links, images


def render_gfm(text: str) -> str:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    response = requests.post(
        "https://api.github.com/markdown",
        headers=headers,
        json={"text": text, "mode": "gfm", "context": REPOSITORY},
        timeout=45,
    )
    response.raise_for_status()
    return response.text


def normalize_fragment(value: str) -> str:
    normalized = urllib.parse.unquote(value).lstrip("#")
    while normalized.startswith("user-content-"):
        normalized = normalized.removeprefix("user-content-")
    return normalized


def remove_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def local_path(destination: str) -> Path | None:
    parsed = urllib.parse.urlsplit(destination)
    if parsed.scheme or destination.startswith("//") or destination.startswith("#"):
        return None
    path = urllib.parse.unquote(parsed.path)
    return Path(path) if path else None


structural_errors: set[str] = set()
external_occurrences: Counter[str] = Counter()
render_counts: dict[str, dict[str, int]] = {}

for path in FILES:
    if not path.exists():
        structural_errors.add(f"arquivo ausente: {path}")
        continue

    text = path.read_text(encoding="utf-8")
    if text.count("```") % 2:
        structural_errors.add(f"{path}: quantidade ímpar de delimitadores de código")

    links, images = extract_destinations(text)
    destinations = links + images

    for destination in destinations:
        parsed = urllib.parse.urlsplit(destination)
        if parsed.scheme in {"http", "https"}:
            external_occurrences[destination] += 1
            continue

        candidate = local_path(destination)
        if candidate is not None and not candidate.exists():
            structural_errors.add(f"{path}: caminho local inexistente: {destination}")

    try:
        html = render_gfm(text)
    except Exception as exc:
        structural_errors.add(f"{path}: falha ao renderizar pelo GitHub: {exc}")
        continue

    soup = BeautifulSoup(html, "html.parser")
    rendered_ids = {
        normalize_fragment(tag.get("id", ""))
        for tag in soup.find_all(id=True)
        if tag.get("id")
    }

    for anchor in soup.select('a[href^="#"]'):
        href = anchor.get("href", "")
        target = normalize_fragment(href)
        if target and target not in rendered_ids:
            structural_errors.add(f"{path}: âncora interna não renderizada: {href}")

    stripped = remove_fenced_code(text)
    separator_count = sum(
        1
        for line in stripped.splitlines()
        if re.match(r"^\s*\|?\s*:?-{3,}:?\s*\|", line)
    )
    rendered_tables = len(soup.find_all("table"))
    if separator_count != rendered_tables:
        structural_errors.add(
            f"{path}: {separator_count} tabelas detectadas no Markdown, "
            f"mas {rendered_tables} renderizadas pelo GitHub"
        )

    render_counts[str(path)] = {
        "headings": len(soup.find_all(re.compile(r"^h[1-6]$"))),
        "tables": rendered_tables,
        "images": len(soup.find_all("img")),
        "code_blocks": len(soup.find_all("pre")),
        "links": len(soup.find_all("a")),
    }

    if path.name == "README-pt-BR.md":
        if render_counts[str(path)]["tables"] < 8:
            structural_errors.add("README-pt-BR.md: número inesperadamente baixo de tabelas renderizadas")
        if render_counts[str(path)]["images"] < 20:
            structural_errors.add("README-pt-BR.md: número inesperadamente baixo de imagens renderizadas")
        if render_counts[str(path)]["headings"] < 80:
            structural_errors.add("README-pt-BR.md: número inesperadamente baixo de títulos renderizados")

session = requests.Session()
session.headers.update(
    {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    }
)


def check_url(url: str):
    last_error = ""
    parsed = urllib.parse.urlsplit(url)
    timeout = (20, 35) if parsed.netloc == "web.archive.org" else (8, 20)

    for attempt in range(3):
        try:
            response = session.get(url, allow_redirects=True, timeout=timeout, stream=True)
            status = response.status_code
            final_url = response.url
            response.close()

            if status in {429, 500, 502, 503, 504} and attempt < 2:
                time.sleep(2**attempt)
                continue

            if 200 <= status < 400:
                category = "ok"
            elif status in {401, 403, 405, 406, 418, 429, 451}:
                category = "restricted"
            elif status in {404, 410}:
                category = "broken"
            elif 500 <= status < 600:
                category = "transient"
            else:
                category = "other"

            return url, category, status, final_url, ""
        except requests.RequestException as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            if attempt < 2:
                time.sleep(2**attempt)

    return url, "error", None, "", last_error


urls = sorted(external_occurrences)
results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(check_url, url): url for url in urls}
    for future in concurrent.futures.as_completed(futures):
        results.append(future.result())

results.sort(key=lambda item: (item[1], item[0]))
categories = Counter(item[1] for item in results)

report: list[str] = [
    "# Auditoria de links e renderização pt-BR",
    "",
    f"- URLs externas únicas: **{len(urls)}**",
    f"- Ocorrências de URLs externas: **{sum(external_occurrences.values())}**",
    f"- Links válidos ou redirecionados: **{categories['ok']}**",
    f"- Links com acesso restrito ou rate limit: **{categories['restricted']}**",
    f"- Links definitivamente quebrados (404/410): **{categories['broken']}**",
    f"- Falhas transitórias de servidor: **{categories['transient']}**",
    f"- Erros de conexão: **{categories['error']}**",
    "",
    "## Renderização pelo GitHub",
    "",
]

for file_name, counts in render_counts.items():
    report.append(
        f"- `{file_name}`: {counts['headings']} títulos, {counts['tables']} tabelas, "
        f"{counts['images']} imagens, {counts['code_blocks']} blocos de código e "
        f"{counts['links']} links"
    )

report.extend(["", "## Problemas estruturais", ""])
if structural_errors:
    report.extend(f"- {item}" for item in sorted(structural_errors))
else:
    report.append("- Nenhum problema estrutural encontrado.")

for category, title in [
    ("broken", "Links definitivamente quebrados"),
    ("restricted", "Links com acesso restrito"),
    ("transient", "Falhas transitórias"),
    ("error", "Erros de conexão"),
    ("other", "Outros status HTTP"),
]:
    items = [item for item in results if item[1] == category]
    report.extend(["", f"## {title}", ""])
    if not items:
        report.append("- Nenhum.")
        continue

    for url, _, status, final_url, error in items:
        details = f"HTTP {status}" if status is not None else error
        redirect = f" → {final_url}" if final_url and final_url != url else ""
        report.append(f"- `{url}` — {details}{redirect}")

report_text = "\n".join(report) + "\n"
Path("pt-br-link-render-audit.md").write_text(report_text, encoding="utf-8")
print(report_text)

summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
if summary_path:
    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write(report_text)

if structural_errors or categories["broken"]:
    sys.exit(1)
