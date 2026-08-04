from pathlib import Path

README_PATH = Path("README-pt-BR.md")
REPORT_PATH = Path("pt-br-link-render-audit.md")

readme = README_PATH.read_text(encoding="utf-8")

old_intro = (
    "A tradução do conteúdo principal foi concluída, mantendo a estrutura e o significado "
    "da versão original em inglês. O documento está agora em fase de revisão."
)
new_intro = (
    "A tradução do conteúdo principal, a revisão estrutural e a validação automatizada de "
    "links e renderização foram concluídas. O documento aguarda revisão técnica e linguística "
    "por falantes nativos."
)

old_item = "- [ ] validação de links externos e renderização final."
new_item = "- [x] validação de links externos e renderização final."

if readme.count(old_intro) != 1:
    raise RuntimeError("Introdução do status não foi encontrada exatamente uma vez")
if readme.count(old_item) != 1:
    raise RuntimeError("Item de validação final não foi encontrado exatamente uma vez")

readme = readme.replace(old_intro, new_intro, 1)
readme = readme.replace(old_item, new_item, 1)

if old_item in readme:
    raise RuntimeError("O item pendente de validação ainda está presente")

README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
REPORT_PATH.unlink(missing_ok=True)
