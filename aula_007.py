# Shorthands
# \w - Todas as letras e números (parecido  com [a-zA-Z0-9À-ú]+)
#      cuidado com a flag re.A (ou re.ASCII), que vai ignorar caracteres br.
# \w -> [a-zA-Z0-9À-ú]
# \W -> [^a-zA-Z0-9À-ú]
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\t\f\v]
# \S -> [^ \r\n\t\f\v]
# \b -> borda: define uma inicialização e finalização de palavra
# \B -> não borda


import re

texto: str = (
    'João trouxe flores para sua amada namorada em 10 de janeiro de 1970. '
    'Maria era o nome dela.\n\n'

    'Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos '
    'atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de '
    'queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca'
    ' esquece seu famoso pão de queijo.\n\n'

    'Não canso de ouvir a Maria: Jooooooooooãoooooooo, o café tá prontinho '
    'aqui. Veeemm!'
)
# print(re.findall(r'[a-z]+', texto))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\w+', texto, flags=re.ASCII))
# print(re.findall(r'\W+', texto, flags=re.ASCII))
# print(re.findall(r'\d+', texto))
# print(re.findall(r'\D+', texto))
# print(re.findall(r'\s+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\be\w+', texto, re.I))
# print(re.findall(r'\w+e\b', texto, re.I))
# print(re.findall(r'\b\w{4}\b', texto, re.I))
print(re.findall(r'flo\B', texto, re.I))
