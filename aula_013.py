import re

senha_forte_regexp = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$',
    flags=re.M
)

senhas = '''
VÁLIDAS
9)AuA,O3e~1h  
}JJ5P\\0mz|8f  
d1BQq3E@`}1j  
1eu~;X58k*WO  
I7cb<|KW1\l9  

SEM MINÚSCULAS
5}A=<6T36:FI  
4X|QUB551`:!  
0P}#01<D`9WD  
22`E#{XP8^6Z
}\BJV;53X/31

SEM MINÚSCULAS E NÚMEROS
~`$REQ<BK:<M
S=Q|~$WCIO\}
LNLD|[*~?X:I
['.K!^MJV?KL
W`|_I:VC~H[C

SEM NÚMEROS CARACTERES E MINÚSCULAS
NDMNWICUUXSJ
HWVJNUBBYTSZ
BAPPPQOSZAET
JOZEHKLWPZYM
OUFFPWEFJDGI

QUANTIDADE INVÁLIDA (6)
c6Q0|h
96~Wrn
20iGh@
81}knG
V4gn5<
'''

for senha in senha_forte_regexp.findall(senhas):
    print(senha)
