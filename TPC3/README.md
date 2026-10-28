# TPC3: Analisador Léxico para Linguagem de Consulta

## Autor
- **Nome:** David João Oliveira Gonçalves
- **ID:** a81820
- [**Foto**](https://raw.githubusercontent.com/David81820/PLC2026/refs/heads/main/TP1/foto_UM.jpeg)

<br>

## Resumo
Neste trabalho foi pedido que se escrevesse em Python um analisador léxico para uma linguagem de consulta tipo SPARQL.

O programa deverá receber strings como o seguinte exemplo:
```py
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

E deverá transformá-las em sequências de tokens:
```py
[
  ("SELECT", "select"),
  ("VAR", "?nome"),
  ("VAR", "?desc"),
  ("WHERE", "where"),
  ("PUNCT", "{"),
  ("VAR", "?s"),
  ("A", "a"),
  ("PREFIX", "dbo:MusicalArtist"),
  ("PUNCT", "."),
  ...
  ("LIMIT", "LIMIT"),
  ("NUM", "1000")
]
```


<br>

## Lista de resultados
* [Analisador Léxico em Python](lex-query.py)