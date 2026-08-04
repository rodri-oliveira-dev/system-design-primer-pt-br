from __future__ import annotations

import re
import urllib.parse
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

FILES = [Path("README-pt-BR.md"), Path("CONTRIBUTING-pt-BR.md"), Path("CONTRIBUTING.md")]
REPORT_PATH = Path("pt-br-link-render-audit.md")

md = MarkdownIt("commonmark", {"html": True})


def walk(tokens):
    for token in tokens:
        yield token
        if token.children:
            yield from walk(token.children)


def normalize_fragment(value: str) -> str:
    normalized = urllib.parse.unquote(value).lstrip("#")
    while normalized.startswith("user-content-"):
        normalized = normalized.removeprefix("user-content-")
    return normalized


def slug_base(text: str) -> str:
    cleaned = []
    for char in text.strip().lower():
        if char.isalnum() or char in {" ", "-", "_"}:
            cleaned.append(char)
    return "".join(cleaned).replace(" ", "-")


def source_anchors_and_links(text: str) -> tuple[set[str], list[str]]:
    tokens = md.parse(text)
    anchors = {
        normalize_fragment(value)
        for value in re.findall(r'<a\s+[^>]*id=["\']([^"\']+)["\']', text, flags=re.I)
    }

    slug_counts: Counter[str] = Counter()
    for index, token in enumerate(tokens):
        if token.type != "heading_open" or index + 1 >= len(tokens):
            continue
        inline = tokens[index + 1]
        if inline.type != "inline":
            continue
        rendered_inline = md.renderInline(inline.content)
        heading_text = BeautifulSoup(rendered_inline, "html.parser").get_text(" ", strip=True)
        base = slug_base(heading_text)
        occurrence = slug_counts[base]
        slug_counts[base] += 1
        slug = base if occurrence == 0 else f"{base}-{occurrence}"
        anchors.add(slug)

    internal_links: list[str] = []
    for token in walk(tokens):
        if token.type == "link_open":
            href = token.attrGet("href")
            if href and href.startswith("#"):
                internal_links.append(href)

    internal_links.extend(
        href
        for href in re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', text, flags=re.I)
        if href.startswith("#")
    )
    return anchors, internal_links


source_errors: set[str] = set()
for path in FILES:
    text = path.read_text(encoding="utf-8")
    anchors, internal_links = source_anchors_and_links(text)
    for href in internal_links:
        target = normalize_fragment(href)
        if target and target not in anchors:
            source_errors.add(f"{path}: âncora interna inexistente na fonte: {href}")

report = REPORT_PATH.read_text(encoding="utf-8")
start_marker = "## Problemas estruturais\n"
end_marker = "\n## Links definitivamente quebrados\n"

start = report.find(start_marker)
end = report.find(end_marker)
if start < 0 or end < 0 or end <= start:
    raise RuntimeError("Não foi possível localizar a seção de problemas estruturais no relatório")

old_section = report[start + len(start_marker) : end]
non_anchor_errors = []
for line in old_section.splitlines():
    stripped = line.strip()
    if not stripped.startswith("- "):
        continue
    if "âncora interna não renderizada" in stripped:
        continue
    if stripped == "- Nenhum problema estrutural encontrado.":
        continue
    non_anchor_errors.append(stripped)

all_errors = sorted(set(non_anchor_errors) | {f"- {error}" for error in source_errors})
new_lines = ["## Problemas estruturais", ""]
if all_errors:
    new_lines.extend(all_errors)
else:
    new_lines.append("- Nenhum problema estrutural encontrado.")
new_section = "\n".join(new_lines) + "\n"

report = report[:start] + new_section + report[end + 1 :]
REPORT_PATH.write_text(report, encoding="utf-8")

if all_errors:
    raise RuntimeError("A validação de âncoras encontrou problemas: " + "; ".join(all_errors))
