# Contribuindo com a tradução para português brasileiro

Obrigado pelo interesse em contribuir com a tradução do **System Design Primer** para português brasileiro.

Este documento descreve o fluxo adotado enquanto a tradução está em andamento no repositório [`rodri-oliveira-dev/system-design-primer-pt-br`](https://github.com/rodri-oliveira-dev/system-design-primer-pt-br).

Para as regras gerais do projeto original, consulte também o [`CONTRIBUTING.md`](CONTRIBUTING.md) em inglês.

## Antes de começar

A versão [`README.md`](README.md) em inglês é a **fonte canônica** do conteúdo. A tradução deve acompanhar seu significado e sua estrutura, sem introduzir conteúdo técnico que ainda não exista no documento original.

Antes de iniciar uma contribuição:

1. Consulte o [status da tradução](README-pt-BR.md#status-da-tradução).
2. Verifique os pull requests e issues abertos para evitar trabalho duplicado.
3. Comente no PR ou na issue correspondente indicando a seção em que pretende trabalhar.
4. Utilize a versão mais recente da branch `docs/pt-br-translation` como base.

## Como você pode contribuir

Você pode ajudar com:

- tradução de seções ainda pendentes;
- revisão técnica de conceitos de arquitetura e sistemas distribuídos;
- revisão linguística em português brasileiro;
- correção de gramática, clareza e fluidez;
- validação de links e âncoras;
- identificação de diferenças entre o `README.md` em inglês e o `README-pt-BR.md`;
- revisão da consistência terminológica.

## Fluxo de contribuição

### 1. Faça um fork deste repositório

Use como origem:

```text
https://github.com/rodri-oliveira-dev/system-design-primer-pt-br
```

### 2. Clone o seu fork

```bash
git clone https://github.com/SEU-USUARIO/system-design-primer-pt-br.git
cd system-design-primer-pt-br
```

### 3. Configure este repositório como upstream

```bash
git remote add upstream https://github.com/rodri-oliveira-dev/system-design-primer-pt-br.git
git fetch upstream
```

### 4. Use a branch de integração da tradução

Enquanto a tradução não estiver concluída, as contribuições devem partir de `docs/pt-br-translation`:

```bash
git switch docs/pt-br-translation
git pull upstream docs/pt-br-translation
```

Não use `master` como base para uma seção da tradução em andamento.

### 5. Crie uma branch específica

Utilize um nome que identifique a seção ou o tipo de alteração:

```bash
git switch -c docs/pt-br-dns-cdn
```

Outros exemplos:

```text
docs/pt-br-databases
docs/pt-br-cache
docs/pt-br-review-terminology
fix/pt-br-broken-links
```

### 6. Faça alterações com escopo reduzido

Sempre que possível, cada pull request deve tratar de uma seção ou de um tipo de revisão. Isso facilita a análise técnica e linguística.

Exemplos de bons escopos:

- traduzir DNS e CDN;
- revisar a terminologia da seção de bancos de dados;
- corrigir links quebrados;
- revisar gramática sem alterar o significado técnico.

### 7. Envie seus commits

Use mensagens de commit objetivas:

```bash
git add README-pt-BR.md
git commit -m "docs(pt-BR): traduz seções de DNS e CDN"
git push -u origin docs/pt-br-dns-cdn
```

### 8. Abra o pull request

Durante o desenvolvimento da tradução, abra o PR com:

```text
base: docs/pt-br-translation
head: sua branch
```

Não direcione o PR para `master` enquanto o `README-pt-BR.md` estiver incompleto.

## Regras de tradução

### Preserve o significado técnico

A tradução deve ser natural em português brasileiro, mas não pode alterar conceitos, garantias, vantagens, desvantagens ou trade-offs apresentados no original.

Quando uma frase parecer tecnicamente ambígua, compare-a com a versão inglesa e explique a decisão no pull request.

### Não traduza estes elementos

Salvo quando houver um motivo claro, preserve:

- blocos de código e comandos;
- nomes de arquivos, diretórios e branches;
- URLs;
- nomes próprios, empresas, produtos e tecnologias;
- siglas consolidadas, como DNS, CDN, TCP, UDP, RPC, REST e CAP;
- títulos de artigos, vídeos, livros e referências externas;
- termos técnicos amplamente utilizados no mercado quando a tradução reduzir a precisão.

### Preserve a estrutura Markdown

Mantenha:

- níveis de títulos;
- listas e tabelas;
- imagens e seus caminhos;
- blocos de código;
- notas e citações;
- referências e links;
- hierarquia das seções.

Após traduzir um título, valide e atualize os links que apontam para sua âncora.

### Terminologia adotada

Use como referência as decisões já registradas no PR de integração. Entre elas:

| Inglês | Forma adotada |
|---|---|
| system design | design de sistemas |
| throughput | throughput; apresentar “vazão” na definição quando útil |
| trade-off | trade-off |
| failover | failover |
| sharding | particionamento horizontal — sharding |
| load balancer | balanceador de carga |
| application layer | camada de aplicação |
| availability | disponibilidade |
| consistency | consistência |
| partition tolerance | tolerância a partições |
| RDBMS | SGBDR, mantendo a sigla original quando necessária |

Caso um termo ainda não tenha uma tradução definida, registre a decisão no PR para que ela possa ser revisada e reutilizada nas demais seções.

### Uso de tradução automática e IA

Ferramentas automáticas podem ser utilizadas como apoio, mas todo conteúdo precisa passar por revisão humana técnica e linguística.

Não envie uma tradução gerada automaticamente sem verificar:

- fidelidade ao texto original;
- precisão dos conceitos;
- consistência com o restante do documento;
- gramática e naturalidade em português brasileiro;
- links, Markdown e âncoras.

## Checklist do pull request

Antes de solicitar revisão, confirme:

- [ ] O PR parte de `docs/pt-br-translation`.
- [ ] O escopo está limitado a uma seção ou tipo de melhoria.
- [ ] A tradução foi comparada com o `README.md` atual em inglês.
- [ ] O significado técnico foi preservado.
- [ ] Código, comandos, URLs e caminhos não foram alterados indevidamente.
- [ ] A terminologia está consistente com as seções anteriores.
- [ ] Títulos e âncoras internas foram validados.
- [ ] Imagens, tabelas, listas e blocos de código continuam renderizando corretamente.
- [ ] O texto foi revisado em português brasileiro.
- [ ] O PR explica decisões terminológicas relevantes.

## Modelo de descrição do pull request

```markdown
## Seção traduzida ou revisada

Descreva o trecho alterado.

## Decisões de terminologia

Liste termos que precisaram de decisão ou contexto.

## Validação

- [ ] Comparado com o README em inglês
- [ ] Links e âncoras revisados
- [ ] Markdown revisado
- [ ] Revisão técnica realizada
- [ ] Revisão linguística realizada
```

## Revisão e créditos

As contribuições serão revisadas antes de serem incorporadas à branch de integração. Mudanças significativas devem receber, sempre que possível:

- uma revisão técnica;
- uma revisão de português brasileiro por falante nativo.

Os autores dos commits e pull requests continuarão registrados no histórico do repositório. Quando conteúdo de traduções anteriores for reutilizado, os créditos correspondentes deverão ser preservados.

## Tradução oficial

A discussão oficial da tradução está na [issue #40 do projeto original](https://github.com/donnemartin/system-design-primer/issues/40).

Quando o `README-pt-BR.md` estiver completo, atualizado e revisado, será preparado um pull request para o repositório original [`donnemartin/system-design-primer`](https://github.com/donnemartin/system-design-primer).