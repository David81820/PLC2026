# TPC2: Conversor de MarkDown para HTML

## Autor
- **Nome:** David João Oliveira Gonçalves
- **ID:** a81820
- [**Foto**](https://raw.githubusercontent.com/David81820/PLC2026/refs/heads/main/TP1/foto_UM.jpeg)

<br>

## Resumo
Neste trabalho foi pedido que se desenvolvesse um programa em Python que substituía os elementos básicos da sintaxe de MarkDown para os elementos equivalentes de sintaxe HTML.

Esses elementos são descritos na secção [*Basic Syntax* da **Markdown Cheat Sheet**](https://www.markdownguide.org/cheat-sheet/#basic-syntax) e incluíem:

| Elemento | MarkDown | HTML |
|---|---|---|
| Cabeçalhos | `# H1`, `## H2`, `### H3` | `<h1>H1</h1>`, `<h2>H2</h2>`, `<h3>H3</h3>` |
| Bold | `**texto**` | `<b>texto</b>` |
| Itálico | `*texto*` | `<i>texto</i>` |
| Citação em Bloco | `> blockquote` | `<blockquote>blockquote</blockquote>` |
| Lista ordenada | `1. item` | `<ol><li>item</li></ol>` |
| Lista não ordernada | `- 1º item` | `<ul><li>1º item</li></ul>` |
| Código | ``código`` | `<code>código</code>`  |
| Linha Horizontal | `---` | `<hr />` |
| Hiperligação | `[texto](url)` | `<a href="url">texto</a>` |
| Imagem | `![alt](endereço)` | `<img src="endereço" alt="alt"/>` |

<br><br>

Explicado da forma mais simples possível:
1. o programa recebe um ficheiro MarkDown de entrada ;
2. o ficheiro é lido linha a linha ;
3. várias expressões regulares são usadas para encontrar elementos da sintaxe MarkDown acima especificada ;
4. quando isso acontece é dada a susbstituição pelo elemento equivalente da sintaxe HTML ;
5. no final é dado o ficheiro HTML resultante da conversão.

<br>

## Lista de resultados
* [programa Python de conversão](conversor-md-html.py)
* [ficheiro exemplo de entrada em MarkDown](input.md)
* [ficheiro exemplo de saída em HTML](output.html)