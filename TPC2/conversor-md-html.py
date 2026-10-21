import re


def cabecalho(linha):
    comp = re.compile(r"^(#|##|###)\s+(.+)")
    
    if comp.match(linha):
        n       = len(comp.match(linha).group(1))
        texto   = comp.match(linha).group(2)

        return f"<h{n}>{texto}</h{n}>"


def negrito(linha):
    comp = re.compile(r"\*\*(.+?)\*\*")

    if comp.search(linha):
        texto = comp.search(linha).group(1)
        return comp.sub(f"<b>{texto}</b>", linha)
    
    return linha


def italico(linha):
    comp = re.compile(r"\*(.+?)\*")

    if comp.search(linha):
        texto = comp.search(linha).group(1)
        return comp.sub(f"<i>{texto}</i>", linha)
    
    return linha


def lista_numerada(linha):
    linha   = linha.splitlines()
    comp    = re.compile(r"\d+\.\s+(.+)$")
    itens   = []

    for l in linha:
        m = comp.match(l)
        if m:
            itens.append(f"<li>{m.group(1)}</li>")
    
    return "<ol>\n" + "\n".join(itens) + "\n</ol>"


def hyperlink(linha):
    comp = re.compile(r"\[(.+?)\]\((.+?)\)")
    return comp.sub(r"<a href=\"\2\">\1</a>",linha)


def imagem(linha):
    comp = re.compile(r"!\[(.+?)\]\((.+?)\)")
    return comp.sub(r"<img src=\"\2\" alt=\"\1\" />", linha)


def lista_nao_ordenada(linha):
    linhas  = linha.splitlines()
    comp    = re.compile(r"^[-*]\s+(.+)$")
    itens   = []

    for l in linhas:
        m = comp.match(l)
        if m:
            itens.append(f"<li>{m.group(1)}</li>")
    
    return "<ul>\n" + "\n".join(itens) + "\n</ul>"





def conversor(input):
    with open(input, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    resultado   = []
    i           = 0

    # vamos ler o ficheiro linha a linha para identificar elementos da sintaxe markdown
    while i < len(linhas):
        linha = linhas[i].rstrip('\n')

        # Verifica se é uma lista numerada
        if re.match(r"\d+\.\s+.+", linha):
            bloco_lista = []
            while i < len(linhas) and re.match(r"\d+\.\s+.+", linhas[i]):
                bloco_lista.append(linhas[i].strip())
                i += 1
            resultado.append(lista_numerada("\n".join(bloco_lista)))
            continue  # já avançou o índice

        # Verifica se é uma lista não ordenada
        if re.match(r"^[-*]\s+.+", linha):
            bloco_lista = []
            while i < len(linhas) and re.match(r"^[-*]\s+.+", linhas[i]):
                bloco_lista.append(linhas[i].strip())
                i += 1
            resultado.append(lista_nao_ordenada("\n".join(bloco_lista)))
            continue  # já avançou o índice

        # Verifica se é uma das restantes possibilidades - cabeçalho, negrito, itálico, hiper-ligação ou imagem
        if cabecalho(linha):
            linha   = cabecalho(linha)
        else:
            linha   = imagem(linha)
            linha   = hyperlink(linha)
            linha   = negrito(linha)
            linha   = italico(linha)

        resultado.append(linha)
        i += 1

    return "\n".join(resultado)


if __name__ == "__main__":
    html = conversor("input.md")
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
