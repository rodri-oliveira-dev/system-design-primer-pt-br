from pathlib import Path
from urllib.parse import unquote
import re

README_PATH = Path("README-pt-BR.md")
CONTRIBUTING_PT_PATH = Path("CONTRIBUTING-pt-BR.md")
CONTRIBUTING_PATH = Path("CONTRIBUTING.md")

readme = README_PATH.read_text(encoding="utf-8")
contributing_pt = CONTRIBUTING_PT_PATH.read_text(encoding="utf-8")
contributing = CONTRIBUTING_PATH.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 trecho, encontrado {count}")
    return text.replace(old, new, 1)


# README: comunicação, fidelidade ao original e consistência editorial.
readme = replace_once(
    readme,
    "**Ajude a [traduzir](https://github.com/donnemartin/system-design-primer/issues/40) este guia!**",
    "**Ajude a [revisar e manter](https://github.com/donnemartin/system-design-primer/issues/40) este guia!**",
    "chamada inicial",
)

readme = replace_once(
    readme,
    "* [Comunicação](#comunicacao)\n    * [Protocolo de Controle de Transmissão — TCP](#protocolo-de-controle-de-transmissao-tcp)",
    "* [Comunicação](#comunicacao)\n    * [Protocolo de Transferência de Hipertexto — HTTP](#protocolo-de-transferencia-de-hipertexto-http)\n    * [Protocolo de Controle de Transmissão — TCP](#protocolo-de-controle-de-transmissao-tcp)",
    "entrada HTTP no índice",
)

readme = replace_once(
    readme,
    "#### CP - consistência e tolerância a partições",
    "#### CP — consistência e tolerância a partições",
    "título CP",
)
readme = replace_once(
    readme,
    "#### AP - disponibilidade e tolerância a partições",
    "#### AP — disponibilidade e tolerância a partições",
    "título AP",
)
readme = replace_once(
    readme,
    "Erro de predição de desvio                       5 ns",
    "Falha de predição de desvio                      5 ns",
    "métrica de branch prediction",
)
readme = replace_once(
    readme,
    "Busca em HDD                              10.000.000 ns",
    "Tempo de busca do HDD                    10.000.000 ns",
    "métrica de HDD seek",
)
readme = replace_once(
    readme,
    "* leitura sequencial da memória principal a 4 GB/s.",
    "* leitura sequencial da memória principal a 4 GB/s;\n* 6 a 7 viagens de ida e volta ao redor do mundo por segundo;\n* 2.000 viagens de ida e volta por segundo dentro de um data center.",
    "métricas de round trip",
)
readme = replace_once(
    readme,
    "* scatter-gather;",
    "* scatter-gather — dispersão e agregação;",
    "explicação de scatter-gather",
)
readme = replace_once(
    readme,
    "- [ ] revisão técnica, linguística, de links e de âncoras.",
    "- [x] revisão estrutural inicial, âncoras internas e comparação com o README original;\n- [ ] revisão técnica e linguística por falantes nativos;\n- [ ] validação de links externos e renderização final.",
    "status da revisão",
)

# Guia em português: transição do fluxo de tradução para revisão e manutenção.
contributing_pt = replace_once(
    contributing_pt,
    "Este documento descreve o fluxo adotado enquanto a tradução está em andamento no repositório [`rodri-oliveira-dev/system-design-primer-pt-br`](https://github.com/rodri-oliveira-dev/system-design-primer-pt-br).",
    "Este documento descreve o fluxo adotado para revisar, manter e atualizar a tradução no repositório [`rodri-oliveira-dev/system-design-primer-pt-br`](https://github.com/rodri-oliveira-dev/system-design-primer-pt-br).",
    "introdução do guia",
)
contributing_pt = replace_once(
    contributing_pt,
    "- tradução de seções ainda pendentes;",
    "- atualização de seções quando o `README.md` original for alterado;",
    "tipos de contribuição",
)
contributing_pt = replace_once(
    contributing_pt,
    "Enquanto a tradução não estiver concluída, as contribuições devem partir de `docs/pt-br-translation`:",
    "Durante a revisão e enquanto o PR de integração permanecer aberto, as contribuições devem partir de `docs/pt-br-translation`:",
    "base das contribuições",
)
contributing_pt = replace_once(
    contributing_pt,
    "Não use `master` como base para uma seção da tradução em andamento.",
    "Não use `master` como base para revisões ou atualizações destinadas ao PR de integração.",
    "restrição de branch",
)
contributing_pt = replace_once(
    contributing_pt,
    "Durante o desenvolvimento da tradução, abra o PR com:",
    "Durante a revisão e a manutenção da tradução, abra o PR com:",
    "abertura de PR",
)
contributing_pt = replace_once(
    contributing_pt,
    "Não direcione o PR para `master` enquanto o `README-pt-BR.md` estiver incompleto.",
    "Não direcione o PR para `master` enquanto o PR de integração da tradução permanecer aberto.",
    "destino do PR",
)
contributing_pt = replace_once(
    contributing_pt,
    "| scatter-gather | scatter-gather; explicar o padrão na primeira ocorrência |",
    "| scatter-gather | scatter-gather — dispersão e agregação; preservar o termo original |",
    "glossário scatter-gather",
)
contributing_pt = replace_once(
    contributing_pt,
    "Quando o `README-pt-BR.md` estiver completo, atualizado e revisado, será preparado um pull request para o repositório original [`donnemartin/system-design-primer`](https://github.com/donnemartin/system-design-primer).",
    "Após a revisão técnica, linguística e estrutural do `README-pt-BR.md`, será preparado um pull request para o repositório original [`donnemartin/system-design-primer`](https://github.com/donnemartin/system-design-primer).",
    "submissão upstream",
)

# Guia geral em inglês: refletir a fase atual sem alterar as regras originais.
contributing = replace_once(
    contributing,
    "Durante o trabalho em andamento, os pull requests de tradução devem usar `docs/pt-br-translation` como branch base.",
    "Durante a fase de revisão e integração, os pull requests da tradução devem usar `docs/pt-br-translation` como branch base.",
    "aviso do CONTRIBUTING em inglês",
)

README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
CONTRIBUTING_PT_PATH.write_text(contributing_pt.rstrip() + "\n", encoding="utf-8")
CONTRIBUTING_PATH.write_text(contributing.rstrip() + "\n", encoding="utf-8")

# Validação estrutural local.
readme = README_PATH.read_text(encoding="utf-8")

if "README.md#" in readme:
    raise RuntimeError("Ainda existem links de seção apontando para o README inglês")

if readme.count("```") % 2 != 0:
    raise RuntimeError("Quantidade ímpar de delimitadores de blocos de código")

explicit_anchors = set(re.findall(r'<a id="([^"]+)"></a>', readme))
heading_anchors = set()
slug_counts: dict[str, int] = {}

for line in readme.splitlines():
    match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
    if not match:
        continue
    heading = re.sub(r"<[^>]+>", "", match.group(1)).strip().lower()
    heading = re.sub(r"[`*_~]", "", heading)
    heading = re.sub(r"[^\w\s-]", "", heading, flags=re.UNICODE)
    heading = re.sub(r"\s+", "-", heading).strip("-")
    base = heading
    occurrence = slug_counts.get(base, 0)
    slug_counts[base] = occurrence + 1
    slug = base if occurrence == 0 else f"{base}-{occurrence}"
    heading_anchors.add(slug)

available_anchors = explicit_anchors | heading_anchors
internal_links = {unquote(value) for value in re.findall(r"\]\(#([^\s)]+)\)", readme)}
missing_anchors = sorted(internal_links - available_anchors)
if missing_anchors:
    raise RuntimeError("Âncoras internas ausentes: " + ", ".join(missing_anchors))

relative_targets = set()
for target in re.findall(r"\]\(([^)]+)\)", readme):
    target = target.strip().split(" ", 1)[0]
    if target.startswith(("http://", "https://", "#", "mailto:")):
        continue
    path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if path_part:
        relative_targets.add(path_part)

for source in re.findall(r'<(?:img|source)[^>]+src="([^"]+)"', readme):
    if not source.startswith(("http://", "https://", "data:")):
        relative_targets.add(unquote(source.split("?", 1)[0]))

missing_files = sorted(path for path in relative_targets if not Path(path).exists())
if missing_files:
    raise RuntimeError("Arquivos locais ausentes: " + ", ".join(missing_files))

required_fragments = [
    "#protocolo-de-transferencia-de-hipertexto-http",
    "6 a 7 viagens de ida e volta ao redor do mundo por segundo",
    "2.000 viagens de ida e volta por segundo dentro de um data center",
    "scatter-gather — dispersão e agregação",
    "revisão estrutural inicial, âncoras internas e comparação com o README original",
]
for fragment in required_fragments:
    if fragment not in readme:
        raise RuntimeError(f"Validação ausente: {fragment}")

print(f"Âncoras explícitas: {len(explicit_anchors)}")
print(f"Âncoras derivadas de títulos: {len(heading_anchors)}")
print(f"Links internos validados: {len(internal_links)}")
print(f"Arquivos locais validados: {len(relative_targets)}")
print("Revisão estrutural inicial concluída com sucesso.")
