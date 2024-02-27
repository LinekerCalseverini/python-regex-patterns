# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
import re

texto: str = (
    '<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>'
)

print(re.findall(r'<[pdiv]{1,3}>(?P<frase>.*)</[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>(?P<frase>.*?)</[pdiv]{1,3}>', texto))
