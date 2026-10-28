import re


def cabecalho(linha):
    comp = re.compile(r"^(#|##|###)\s+(.+)")                # procura cabeçalhos Markdown (#, ## ou ###)
    
    m = comp.match(linha)

    if m:                                                   # se a linha corresponder ao padrão
        n       = len(m.group(1))                           # número de # determina o nível do cabeçalho
        texto   = m.group(2)                                # texto do cabeçalho
        
        return f"<h{n}>{texto}</h{n}>"                      # substitui pela etiqueta HTML correspondente


def negrito(linha):
    comp = re.compile(r"\*\*(.+?)\*\*")                     # procura texto delimitado por **

    return comp.sub(r"<b>\1</b>", linha)                    # substitui todas as ocorrências por <b>...</b>


def italico(linha):
    comp = re.compile(r"\*(.+?)\*")                         # procura texto delimitado por *

    return comp.sub(r"<i>\1</i>", linha)                    # substitui todas as ocorrências por <i>...</i>


def citacao(linha):
    comp = re.compile(r"^>\s+(.+)$")                        # procura uma linha iniciada por >

    m = comp.match(linha)

    if m:
        return f"<blockquote>{m.group(1)}</blockquote>"

    return linha


def lista_numerada(linha):
    linha   = linha.splitlines()                            # divide o bloco em linhas
    
    comp    = re.compile(r"\d+\.\s+(.+)$")                  # procura linhas do tipo "1. texto"
    itens   = []

    for l in linha:                                         # converte cada item em <li>
        m = comp.match(l)
        if m:
            itens.append(f"<li>{m.group(1)}</li>")
    
    return "<ol>\n" + "\n".join(itens) + "\n</ol>"          # envolve todos os itens numa lista ordenada


def lista_nao_ordenada(linha):
    linhas  = linha.splitlines()                            # divide o bloco em linhas
    comp    = re.compile(r"^[-*]\s+(.+)$")                  # procura linhas iniciadas por - ou *
    itens   = []

    for l in linhas:                                        # converte cada item para <li>
        m = comp.match(l)
        if m:
            itens.append(f"<li>{m.group(1)}</li>")
    
    return "<ul>\n" + "\n".join(itens) + "\n</ul>"          # envolve os itens em <ul>


def code(linha):
    comp = re.compile(r"`(.+?)`")                           # procura texto delimitado por um acento grave (`...`)

    return comp.sub(r"<code>\1</code>", linha)              # substitui todas as ocorrências por <code>...</code>


def horizontal(linha):
    comp = re.compile(r"^\s*([-])\1{2,}\s*$")               # procura linhas constituídas por ---

    if comp.match(linha):
        return "<hr />"

    return linha


def hyperlink(linha):
    comp = re.compile(r"\[(.+?)\]\((.+?)\)")                    # procura ligações [texto](url)
    return comp.sub(r"<a href=\"\2\">\1</a>",linha)             # converte para <a href="url">texto</a>


def imagem(linha):
    comp = re.compile(r"!\[(.+?)\]\((.+?)\)")                   # procura ![alt](endereço)
    return comp.sub(r"<img src=\"\2\" alt=\"\1\" />", linha)    # converte para <img src="endereço" alt="alt"/>





def conversor(input):
    with open(input, 'r', encoding='utf-8') as f:               # lê todo o ficheiro MarkDown para memória
        linhas = f.readlines()
    
    resultado   = []
    i           = 0

    # vamos ler o ficheiro linha a linha para identificar elementos da sintaxe markdown
    while i < len(linhas):
        linha = linhas[i].rstrip('\n')                                  # remove o carácter '\n'

        # verifica se é uma lista numerada
        if re.match(r"\d+\.\s+.+", linha):
            bloco_lista = []
            while i < len(linhas) and re.match(r"\d+\.\s+.+", linhas[i]):
                bloco_lista.append(linhas[i].strip())
                i += 1
            resultado.append(lista_numerada("\n".join(bloco_lista)))
            continue                                                    # já avançou o índice

        # verifica se é uma lista não ordenada
        if re.match(r"^[-*]\s+.+", linha):
            bloco_lista = []
            while i < len(linhas) and re.match(r"^[-*]\s+.+", linhas[i]):
                bloco_lista.append(linhas[i].strip())
                i += 1
            resultado.append(lista_nao_ordenada("\n".join(bloco_lista)))
            continue  # já avançou o índice

        # verifica se é uma das restantes possibilidades
        if cabecalho(linha):
            linha   = cabecalho(linha)
        else:
            linha   = horizontal(linha)
            linha   = hyperlink(linha)
            linha   = negrito(linha)
            linha   = italico(linha)
            linha   = citacao(linha)
            linha   = imagem(linha)
            linha   = code(linha)

        # guarda a linha convertida
        resultado.append(linha)
        i += 1

    # junta todas as linhas HTML produzidas
    return "\n".join(resultado)


if __name__ == "__main__":
    html = conversor("input.md")
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
