import re

regex = r"^(?!.*011)[01]*$"

testes = [
    "1111111111111111",     # válida
    "0000000000000000",     # válida
    "1011",
    "10101010101010",       # válida
    "1000",                 # válida
    "10100",                # válida
    "011",
    "1110110",
    "101",                  # válida
    "00001010111",
    "101010101011",
    "1101010",              # válida
    "0110000",
    "1000011",
    "110111",
    "1110001",              # válida
    "011011",
]

for string in testes:
    resultado = bool(re.fullmatch(regex, string))
    print(f"{string:<18} sequência válida?  {resultado}")
