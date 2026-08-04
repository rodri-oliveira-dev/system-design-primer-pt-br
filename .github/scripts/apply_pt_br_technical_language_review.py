from pathlib import Path

readme_path = Path("README-pt-BR.md")
readme = readme_path.read_text(encoding="utf-8")

old = "* **CNAME — canonical name** — aponta um nome para outro nome, que pode apontar para outro `CNAME` ou para um registro `A`, como no redirecionamento de `example.com` para `www.example.com`."
new = "* **CNAME — canonical name** — aponta um nome para outro nome, que pode apontar para outro `CNAME` ou para um registro `A`, como ao associar `example.com` a `www.example.com`."

count = readme.count(old)
if count != 1:
    raise RuntimeError(f"CNAME: esperado 1 trecho, encontrados {count}")

readme = readme.replace(old, new, 1)
readme_path.write_text(readme.rstrip() + "\n", encoding="utf-8")
