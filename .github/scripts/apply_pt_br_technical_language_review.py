from pathlib import Path

README_PATH = Path("README-pt-BR.md")
CONTRIBUTING_PATH = Path("CONTRIBUTING-pt-BR.md")

readme = README_PATH.read_text(encoding="utf-8")
contributing = CONTRIBUTING_PATH.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: esperado 1 trecho, encontrados {count}")
    return text.replace(old, new, 1)


readme_replacements = [
    (
        "* [Traduzir](https://github.com/donnemartin/system-design-primer/issues/40).",
        "* [Revisar e manter a tradução](https://github.com/donnemartin/system-design-primer/issues/40).",
        "chamada de contribuição",
    ),
    (
        "> Como conduzir uma pergunta de entrevista de design de sistemas.",
        "> Como conduzir a discussão de uma pergunta de entrevista de design de sistemas.",
        "descrição da entrevista",
    ),
    ("* Quantos usuários existirão?", "* Quantos usuários o sistema terá?", "quantidade de usuários"),
    (
        "* Qual volume de dados esperamos processar?",
        "* Qual volume de dados esperamos que o sistema processe?",
        "volume de dados",
    ),
    (
        "Esboce um design de alto nível contendo todos os componentes importantes.",
        "Esboce um design de alto nível que inclua todos os componentes importantes.",
        "design de alto nível",
    ),
    (
        "* A conversão de uma URL com hash para a URL completa:",
        "* A conversão do hash de uma URL em sua URL completa:",
        "conversão de URL",
    ),
    (
        "Talvez seja solicitado que você faça algumas estimativas manualmente.",
        "Talvez você precise fazer algumas estimativas à mão.",
        "estimativas manuais",
    ),
    (
        "Depois de uma escrita, as leituras podem ou não enxergar a alteração.",
        "Depois de uma escrita, as leituras podem ou não refletir a alteração.",
        "consistência fraca",
    ),
    (
        "Depois de uma escrita, as leituras acabarão enxergando a alteração, normalmente em alguns milissegundos.",
        "Depois de uma escrita, as leituras acabarão refletindo a alteração, normalmente em alguns milissegundos.",
        "consistência eventual",
    ),
    (
        "Depois de uma escrita, as leituras enxergarão a alteração.",
        "Depois de uma escrita, as leituras refletirão a alteração.",
        "consistência forte",
    ),
    (
        "Aguardar uma resposta do nó isolado pela partição pode resultar em um erro de timeout.",
        "Aguardar a resposta de um nó isolado por uma partição de rede pode resultar em um erro de timeout.",
        "CAP CP",
    ),
    (
        "ou quando o sistema precisa continuar funcionando apesar de erros externos.",
        "ou quando o sistema precisa continuar funcionando apesar de falhas externas.",
        "CAP AP",
    ),
    (
        "A duração da indisponibilidade depende de o servidor passivo já estar executando em espera *hot standby* ou precisar ser iniciado a partir de uma espera *cold standby*.",
        "A duração da indisponibilidade depende de o servidor passivo já estar em execução no modo *hot standby* ou precisar ser iniciado a partir do modo *cold standby*.",
        "hot e cold standby",
    ),
    (
        "Seu roteador ou provedor de internet fornece informações sobre quais servidores DNS devem ser consultados durante uma resolução.",
        "O roteador ou o provedor de internet informa quais servidores DNS devem ser consultados durante a resolução.",
        "resolução DNS",
    ),
    (
        "* **CNAME — canonical name** — aponta um nome para outro nome ou `CNAME`, como `example.com` para `www.example.com`, ou para um registro `A`.",
        "* **CNAME — canonical name** — aponta um nome para outro nome, que pode apontar para outro `CNAME` ou para um registro `A`, como no redirecionamento de `example.com` para `www.example.com`.",
        "registro CNAME",
    ),
    (
        "Servir conteúdo por CDNs pode melhorar significativamente o desempenho de duas maneiras:",
        "Distribuir conteúdo por meio de CDNs pode melhorar significativamente o desempenho de duas maneiras:",
        "distribuição por CDN",
    ),
    (
        "* impedir que requisições sejam enviadas a servidores não saudáveis;",
        "* impedir que requisições sejam enviadas a servidores com falhas ou indisponíveis;",
        "integridade no balanceamento",
    ),
    (
        "Esses balanceadores encerram o tráfego de rede, leem a mensagem, tomam a decisão de balanceamento e abrem uma conexão com o servidor selecionado.",
        "Esses balanceadores terminam a conexão de rede, leem a mensagem, tomam a decisão de balanceamento e abrem uma nova conexão com o servidor selecionado.",
        "balanceamento L7",
    ),
    (
        "tráfego sensível de cobrança",
        "tráfego sensível de faturamento",
        "faturamento",
    ),
    (
        "hardware comum moderno",
        "hardware moderno de uso geral",
        "hardware de uso geral",
    ),
    (
        "* os servidores devem ser stateless, sem armazenar dados relacionados ao usuário, como sessões ou fotos de perfil;",
        "* os servidores devem ser stateless (sem estado), sem armazenar dados relacionados ao usuário, como sessões ou fotos de perfil;",
        "stateless",
    ),
    (
        "[Health checks](https://www.consul.io/intro/getting-started/checks.html) ajudam a verificar a integridade dos serviços",
        "[Verificações de integridade — health checks](https://www.consul.io/intro/getting-started/checks.html) ajudam a verificar a integridade dos serviços",
        "health checks",
    ),
    (
        "O uso de cache melhora o tempo de carregamento das páginas e pode reduzir a carga sobre servidores e bancos de dados. Nesse modelo, o componente responsável por despachar a requisição verifica primeiro se ela já foi realizada e tenta localizar um resultado anterior para devolvê-lo, evitando uma nova execução.",
        "O uso de cache melhora o tempo de carregamento das páginas e pode reduzir a carga sobre servidores e bancos de dados. Nesse modelo, o componente que atende à requisição verifica primeiro se existe um resultado anterior armazenado e o devolve, evitando uma nova execução.",
        "introdução de cache",
    ),
    (
        "A RAM é mais limitada do que o disco; por isso, algoritmos de [invalidação de cache](https://en.wikipedia.org/wiki/Cache_algorithms), como [least recently used — LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)), ajudam a remover entradas *cold* e manter dados *hot* na memória.",
        "A RAM é mais limitada do que o disco; por isso, políticas de [substituição de cache](https://en.wikipedia.org/wiki/Cache_replacement_policies), como [least recently used — LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)), ajudam a remover entradas *cold* e manter dados *hot* na memória.",
        "política LRU",
    ),
    (
        "Em geral, evite caches baseados em arquivos, pois eles dificultam a clonagem de servidores e o auto scaling.",
        "Em geral, evite caches baseados em arquivos, pois eles dificultam a clonagem de servidores e o auto scaling (escalabilidade automática).",
        "auto scaling",
    ),
    (
        "* quando um dado é alterado, como uma célula de uma tabela, é necessário remover todas as consultas armazenadas que possam conter o valor modificado.",
        "* quando um dado é alterado, como o valor de uma coluna em determinada linha, é necessário remover todas as consultas armazenadas que possam conter o valor modificado.",
        "célula de tabela",
    ),
    (
        "* essa abordagem permite processamento assíncrono: workers montam objetos consumindo a versão mais recente armazenada em cache.",
        "* essa abordagem permite processamento assíncrono: workers montam objetos a partir da versão mais recente armazenada em cache.",
        "cache de objetos",
    ),
    ("* a operação retorna.", "* a operação é concluída.", "write-through"),
    (
        "Eles também permitem realizar antecipadamente trabalhos demorados, como agregações periódicas de dados.",
        "Eles também permitem executar antecipadamente tarefas demoradas, como agregações periódicas de dados.",
        "assincronismo",
    ),
    (
        "O **[RabbitMQ](https://www.rabbitmq.com/)** é popular, mas exige adaptação ao protocolo AMQP e o gerenciamento dos próprios nós.",
        "O **[RabbitMQ](https://www.rabbitmq.com/)** é popular, mas exige que a aplicação adote o protocolo AMQP e que a equipe gerencie os próprios nós.",
        "RabbitMQ",
    ),
    (
        "A repetição pode utilizar [backoff exponencial](https://en.wikipedia.org/wiki/Exponential_backoff).",
        "As novas tentativas podem utilizar [backoff exponencial](https://en.wikipedia.org/wiki/Exponential_backoff).",
        "backoff exponencial",
    ),
    (
        "Em uma RPC, um cliente provoca a execução de um procedimento em outro espaço de endereçamento, normalmente em um servidor remoto.",
        "Em uma RPC, um cliente solicita a execução de um procedimento em outro espaço de endereçamento, normalmente em um servidor remoto.",
        "definição de RPC",
    ),
    (
        '  "data":"anId";\n  "anotherdata": "another value"',
        '  "data": "anId",\n  "anotherdata": "another value"',
        "JSON RPC",
    ),
    (
        '"personid": "1234";<br/>"itemid": "456"',
        '"personid": "1234",<br/>"itemid": "456"',
        "JSON tabela personid",
    ),
    (
        '"itemid": "456";<br/>"key": "value"',
        '"itemid": "456",<br/>"key": "value"',
        "JSON tabela itemid",
    ),
    (
        "* **[HATEOAS](http://restcookbook.com/Basics/hateoas/) — interface HTML para HTTP** — o serviço web deve ser completamente acessível por um navegador.",
        "* **[HATEOAS](http://restcookbook.com/Basics/hateoas/) — hipermídia como motor do estado da aplicação** — as respostas incluem links que orientam o cliente sobre as ações e transições disponíveis.",
        "HATEOAS",
    ),
    (
        "REST adota uma forma mais genérica e uniforme de expor recursos por URIs, [representações por cabeçalhos](https://github.com/for-GET/know-your-http-well/blob/master/headers.md) e ações por verbos como GET, POST, PUT, DELETE e PATCH.",
        "REST adota uma forma mais genérica e uniforme de expor recursos por URIs, representações negociadas por [cabeçalhos](https://github.com/for-GET/know-your-http-well/blob/master/headers.md) e corpos de mensagem, e ações por verbos como GET, POST, PUT, DELETE e PATCH.",
        "representações REST",
    ),
    (
        "essas várias viagens são especialmente indesejáveis.",
        "essas várias idas e voltas são especialmente indesejáveis.",
        "round trips REST",
    ),
    (
        "* Valide e sanitize todas as entradas de usuários, assim como qualquer parâmetro de entrada exposto a eles, para evitar",
        "* Valide e sanitize todos os dados fornecidos pelos usuários, assim como qualquer parâmetro que eles possam controlar, para evitar",
        "sanitização de entradas",
    ),
    (
        "Em algumas entrevistas, você poderá ser solicitado a realizar estimativas de ordem de grandeza",
        "Em algumas entrevistas, poderão pedir que você realize estimativas de ordem de grandeza",
        "introdução do apêndice",
    ),
    (
        "- [x] revisão estrutural inicial, âncoras internas e comparação com o README original;\n- [ ] revisão técnica e linguística por falantes nativos;",
        "- [x] revisão estrutural inicial, âncoras internas e comparação com o README original;\n- [x] primeira passagem técnica e linguística assistida;\n- [ ] revisão técnica e linguística por falantes nativos;",
        "status da revisão",
    ),
]

for old, new, label in readme_replacements:
    readme = replace_once(readme, old, new, label)

contributing = replace_once(
    contributing,
    "Quando uma frase parecer tecnicamente ambígua, compare-a com a versão inglesa e explique a decisão no pull request.",
    "Quando uma frase parecer tecnicamente ambígua, compare-a com a versão inglesa e explique a decisão no pull request. Correções de imprecisões técnicas presentes no original devem ser claramente identificadas e justificadas, sem alterar silenciosamente o escopo do conteúdo.",
    "orientação para correções técnicas",
)

contributing = replace_once(
    contributing,
    "| connection pool | pool de conexões |",
    "| connection pool | pool de conexões |\n| health check | verificação de integridade — health check |\n| cache replacement policy | política de substituição de cache |\n| HATEOAS | hipermídia como motor do estado da aplicação — HATEOAS |",
    "novos termos do glossário",
)

README_PATH.write_text(readme.rstrip() + "\n", encoding="utf-8")
CONTRIBUTING_PATH.write_text(contributing.rstrip() + "\n", encoding="utf-8")
