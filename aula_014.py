import re

numeros = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''


def is_float(string: str) -> bool:
    return bool(re.search(r'^(?:\+|-)?\d+(?:\.\d+)?$', string))


def is_int(string: str) -> bool:
    return bool(re.search(r'^(?:\+|-)?\d+$', string))


for numero in re.split(r'\n', numeros):
    if is_float(numero):
        print(f'{numero} e um número real')
        continue

    if is_int(numero):
        print(f'{numero} e um número inteiro')
        continue

    print(f'{numero} e um número inválido')
