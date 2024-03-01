# Flags
# A -> Ascii-only
# I -> Ignore Case
# M -> Multiline
# S -> Dotall
import re

texto: str = '''
184.230.500-09
597.628.560-07
794.620.970-38
'''

# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, re.M))

texto2: str = 'O João gosta de folia \n E adora ser amado'

print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
