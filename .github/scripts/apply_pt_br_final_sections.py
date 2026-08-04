from pathlib import Path

readme_path = Path("README-pt-BR.md")
contributing_path = Path("CONTRIBUTING-pt-BR.md")

readme = readme_path.read_text(encoding="utf-8")
contributing = contributing_path.read_text(encoding="utf-8")

if '<a id="em-desenvolvimento"></a>' in readme:
    raise RuntimeError("As seções finais já foram adicionadas")

replacements = {
    "> Esta tradução para português brasileiro está em andamento e acompanha o [`README.md`](README.md) original em inglês. Contribuições e revisões técnicas são bem-vindas por meio de pull requests neste repositório.":
    "> A tradução principal para português brasileiro foi concluída e acompanha o [`README.md`](README.md) original em inglês. O conteúdo está em fase de revisão técnica e linguística, e contribuições são bem-vindas por meio de pull requests neste repositório.",
    "O conteúdo que ainda precisa de melhorias está indicado como [em desenvolvimento](README.md#under-development) na versão original.":
    "O conteúdo que ainda precisa de melhorias está indicado na seção [Em desenvolvimento](#em-desenvolvimento).",
    "> As seções já traduzidas apontam para este documento. As demais continuam apontando temporariamente para o `README.md` original em inglês.":
    "> A tradução principal está concluída. Todos os itens do índice abaixo apontam para seções deste documento.",
    "* [Em desenvolvimento](README.md#under-development)": "* [Em desenvolvimento](#em-desenvolvimento)",
    "* [Créditos](README.md#credits)": "* [Créditos](#creditos)",
    "* [Informações de contato](README.md#contact-info)": "* [Informações de contato](#informacoes-de-contato)",
    "* [Licença](README.md#license)": "* [Licença](#licenca)",
}

for old, new in replacements.items():
    if old not in readme:
        raise RuntimeError(f"Trecho esperado não encontrado: {old}")
    readme = readme.replace(old, new, 1)

marker = "\n## Status da tradução\n"
if marker not in readme:
    raise RuntimeError("Marcador de status não encontrado")

final_sections = r'''
<a id="em-desenvolvimento"></a>
## Em desenvolvimento

Tem interesse em adicionar uma seção ou ajudar a concluir uma que está em andamento? [Contribua](#como-contribuir)!

* Computação distribuída com MapReduce;
* hashing consistente;
* scatter-gather;
* [contribua](#como-contribuir).

<a id="creditos"></a>
## Créditos

Os créditos e as fontes são apresentados ao longo deste repositório.

Agradecimentos especiais a:

* [Hired in tech](http://www.hiredintech.com/system-design/the-system-design-process/)
* [Cracking the coding interview](https://www.amazon.com/dp/0984782850/)
* [High scalability](http://highscalability.com/)
* [checkcheckzz/system-design-interview](https://github.com/checkcheckzz/system-design-interview)
* [shashank88/system_design](https://github.com/shashank88/system_design)
* [mmcgrana/services-engineering](https://github.com/mmcgrana/services-engineering)
* [System design cheat sheet](https://gist.github.com/vasanthk/485d1c25737e8e72759f)
* [A distributed systems reading list](http://dancres.github.io/Pages/)
* [Cracking the system design interview](http://www.puncsky.com/blog/2016-02-13-crack-the-system-design-interview)

<a id="informacoes-de-contato"></a>
## Informações de contato

Sinta-se à vontade para entrar em contato comigo para discutir problemas, dúvidas ou comentários.

Minhas informações de contato estão disponíveis na minha [página do GitHub](https://github.com/donnemartin).

<a id="licenca"></a>
## Licença

*Disponibilizo a você o código e os recursos deste repositório sob uma licença open source. Como este é meu repositório pessoal, a licença sobre meu código e meus recursos é concedida por mim, e não pelo meu empregador (Facebook).*

    Copyright 2017 Donne Martin

    Licença Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)

    http://creativecommons.org/licenses/by/4.0/
'''

readme = readme.replace(marker, "\n" + final_sections.strip() + "\n" + marker, 1)

status_replacements = {
    "A tradução está sendo desenvolvida incrementalmente, mantendo a estrutura e o significado da versão original em inglês.":
    "A tradução do conteúdo principal foi concluída, mantendo a estrutura e o significado da versão original em inglês. O documento está agora em fase de revisão.",
    "- [ ] créditos, informações de contato e licença;":
    "- [x] seção em desenvolvimento, créditos, informações de contato e licença;",
}
for old, new in status_replacements.items():
    if old not in readme:
        raise RuntimeError(f"Linha de status não encontrada: {old}")
    readme = readme.replace(old, new, 1)

glossary_marker = "| company engineering blog | blog de engenharia de empresa |"
glossary_addition = """| company engineering blog | blog de engenharia de empresa |
| distributed computing | computação distribuída |
| consistent hashing | hashing consistente |
| scatter-gather | scatter-gather; explicar o padrão na primeira ocorrência |
| open source license | licença open source |
| contact info | informações de contato |"""
if glossary_marker not in contributing:
    raise RuntimeError("Marcador do glossário não encontrado")
contributing = contributing.replace(glossary_marker, glossary_addition, 1)

readme_path.write_text(readme.rstrip() + "\n", encoding="utf-8")
contributing_path.write_text(contributing.rstrip() + "\n", encoding="utf-8")
