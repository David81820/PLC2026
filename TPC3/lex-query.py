import re
from collections import namedtuple


Token = namedtuple("Token", ["type", "value"])


token_regex = [
    ('COMMENT',     r'#.*'),                    # comentários
    ('SELECT',      r'(?i:\bSELECT\b)'),         # palavra-chave SELECT
    ('WHERE',       r'(?i:\bWHERE\b)'),          # palavra-chave WHERE
    ('LIMIT',       r'(?i:\bLIMIT\b)'),          # palavra-chave LIMIT
    ('A',           r'\ba\b'),                 # 'a' (atalho para rdf:type)
    ('VAR',         r'\?[a-zA-Z_][\w]*'),       # variáveis (ex.: ?nome)
    ('PREFIX',      r'[a-zA-Z_][\w-]*:[\w-]+'), # prefixos (ex.: dbo:MusicalArtist)
    ('STRING',      r'"[^"]*"'),                # literais entre aspas (ex.: "Chuck Berry)
    ('LANGTAG',     r'@[a-zA-Z-]+'),            # etiquetas de linguaguem (ex.: @en)
    ('NUM',         r'\d+'),                    # números
    ('PUNCT',       r'[{}.;]'),                 # pontuação da query
    ('WHITESPACE',  r'\s+'),                    # espaços em branco (ignorados)
    ('ERROR',       r'.'),                      # qualquer outro tipo de caracter (erro)
]


master_pattern = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_regex)
)


def tokenize(code):
    tokens = []

    for match in master_pattern.finditer(code):
        kind    = match.lastgroup
        value   = match.group()

        if kind == "WHITESPACE" or kind == "COMMENT":
            continue
        elif kind == "ERROR":
            raise SyntaxError(f"Caractere inesperado: {value!r}")
        
        tokens.append(Token(kind.upper(), value))
    
    return tokens


query = '''
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
   ?s a dbo:MusicalArtist.
   ?s foaf:name "Chuck Berry"@en .
   ?w dbo:artist ?s.
   ?w foaf:name ?nome.
   ?w dbo:abstract ?desc
} LIMIT 1000
'''

for tok in tokenize(query):
    print(tok)
