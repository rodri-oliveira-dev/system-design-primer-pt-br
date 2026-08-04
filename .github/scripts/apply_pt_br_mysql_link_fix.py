from pathlib import Path

README_PATH = Path("README-pt-BR.md")
REPORT_PATH = Path("pt-br-link-render-audit.md")

readme = README_PATH.read_text(encoding="utf-8")
old = "* [Tips for optimizing MySQL queries](http://aiddroid.com/10-tips-optimizing-mysql-queries-dont-suck/)"
new = "* [Optimizing SQL statements](https://dev.mysql.com/doc/refman/8.4/en/statement-optimization.html)"

count = readme.count(old)
if count != 1:
    raise RuntimeError(f"link de otimização MySQL: esperado 1 trecho, encontrados {count}")

readme = readme.replace(old, new, 1)
if "aiddroid.com/10-tips-optimizing-mysql-queries-dont-suck" in readme:
    raise RuntimeError("URL inacessível do Aiddroid ainda está presente")

README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
REPORT_PATH.unlink(missing_ok=True)
