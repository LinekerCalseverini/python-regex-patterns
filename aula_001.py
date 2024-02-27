import re

string = 'Este é um teste de expressões regulares.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string))

pattern = re.compile(r'teste')

print(pattern.search(string))
print(pattern.findall(string))
print(pattern.sub('ABCD', string))
