# Meta caracteres:
# ^ - Começa com
# $ - Termina com
# [^.*] - Negação

import re


cpf: str = '147.852.963-12'
print(re.findall(r'^(?:\d{3}\.){2}\d{3}-\d{2}$', cpf))
print(re.findall(r'[^0-9]+', cpf))
