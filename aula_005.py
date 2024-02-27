# Meta caracteres: ^ $
# ( )         \1
# ( ) ( )     \1 \2
# ( ( ) ) ( ) \1 \2 \3

# ?: Operador de exclusão de grupo
# ?P< > Operador para nomear o grupo
# (?P= ) Operador para referenciar o grupo pelo nome

import re


texto: str = (
    '<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>'
)
# cpf: str = '147.852.963-12'
# print(re.findall(r'(?:\d{3}\.){2}\d{3}-\d{2}', cpf))

# print(re.findall(r'(<([pdiv]{1,3})>(.*?)</\2>)', texto))
# print(re.findall(r'(<(?P<tag>[pdiv]{1,3})>(.*?)<\/(?P=tag))', texto))

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))
