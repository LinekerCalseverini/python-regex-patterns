import re

cpf = '147.852.963-12'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile(
    r'^((1?\d{1,2}|2[0-4]\d|25[0-5])\.\2\.\2\.\2$)',
    flags=re.X
)

for i in range(300):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
