from pathlib import Path

README_PATH = Path("README-pt-BR.md")
REPORT_PATH = Path("pt-br-link-render-audit.md")

readme = README_PATH.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 trecho, encontrados {count}")
    return text.replace(old, new, 1)


replacements = [
    (
        "* [Redis architecture](http://qnimate.com/overview-of-redis-architecture/)",
        "* [Redis internals](https://redis.io/docs/latest/operate/oss_and_stack/reference/internals/)",
        "Redis internals",
    ),
    (
        '<i><a href="http://www.escotal.com/osilayer.html">Fonte: OSI 7 layer model</a></i>',
        '<i><a href="https://www.cloudflare.com/pt-br/learning/ddos/glossary/open-systems-interconnection-model-osi/">Referência: O que é o modelo OSI?</a></i>',
        "modelo OSI",
    ),
    (
        "[Salesforce Engineering Blog](https://developer.salesforce.com/blogs/engineering/)",
        "[Salesforce Engineering Blog](https://engineering.salesforce.com/)",
        "Salesforce Engineering Blog",
    ),
    (
        'href="https://smartbear.com/learn/api-design/what-are-microservices"',
        'href="https://smartbear.com/learn/api-design/microservices/?lang=en-us"',
        "SmartBear microservices",
    ),
    (
        '<i><a href="https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/">Fonte: Why use a CDN</a></i>',
        '<i><a href="https://www.cloudflare.com/pt-br/learning/cdn/cdn-benefits/">Referência: benefícios da CDN</a></i>',
        "benefícios da CDN",
    ),
]

for old, new, label in replacements:
    readme = replace_once(readme, old, new, label)

obsolete_urls = [
    "http://qnimate.com/overview-of-redis-architecture/",
    "http://www.escotal.com/osilayer.html",
    "https://developer.salesforce.com/blogs/engineering/",
    "https://smartbear.com/learn/api-design/what-are-microservices",
    "https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/",
]

remaining = [url for url in obsolete_urls if url in readme]
if remaining:
    raise RuntimeError(f"URLs obsoletas ainda presentes: {remaining}")

README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
REPORT_PATH.unlink(missing_ok=True)
