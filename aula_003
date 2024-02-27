# Meta caracteres: ^ $ * + ? { } \ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n} n vezes
# {min, max} - range
# {10,} 10 ou mais
# {,10} de 0 a 10
# {10} apenas 10
# {5, 10} de 5 a 10 vezes
import re

texto: str = (
    'João trouxe flores para sua amada namorada em 10 de janeiro de 1970. '
    'Maria era o nome dela.\n\n'

    'Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos '
    'atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de '
    'queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca'
    ' esquece seu famoso pão de queijo.\n\n'

    'Não canso de ouvir a Maria: Jooooooooooãoooooooo, o café tá prontinho '
    'aqui. Veeemm veeem veem vem!'
)

print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}', texto, flags=re.IGNORECASE))
# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.IGNORECASE))

texto2 = 'João ama ser amado.'
print(re.findall(r'ama[do]{0,2}', texto2, flags=re.IGNORECASE))
