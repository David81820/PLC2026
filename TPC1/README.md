# TPC1: RegEx que exclua a string "011"

## Autor
- **Nome:** David João Oliveira Gonçalves
- **ID:** a81820
- [**Foto**](foto_UM.jpeg)

<br>

## Resumo
Neste trabalho foi pedido a elaboração de uma expressão regular que valida strings binárias, filtrando qualquer entrada que contém a sequência contígua "011".

Para tal propósito definiu-se a especificação `^(?!.*011)[01]*$`, eis o porquê:
- `^` início da string;
- `(?!.*011)` garante que nunca irá aparecer "011";
- `[01]*` aceita qualquer sequência binária;
- `$` fim da string. 

<br>

## Lista de resultados
* [script python de teste](test.py)
* [prova de resultados (terminal)](tpc1.png) -- [prova de resultados (site)](tpc1-2.png)