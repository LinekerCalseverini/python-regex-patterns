import re

regex = re.compile(
    r'^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$',
    flags=re.M
)

cpf_list = (
    '147.852.963-12\n'
    '111.111.111-12\n'
    '111.111.111-11\n'
)

print(regex.findall(cpf_list))
