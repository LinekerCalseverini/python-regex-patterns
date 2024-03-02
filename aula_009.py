import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
'''

# Positive Lookahead
# pprint(re.findall(
#     r'\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+(?=active)',
#     texto))

# Negative Lookahead
# pprint(re.findall(
#     r'\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+(?!active)',
#     texto))
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive Lookbehind
pprint(re.findall(
    r'\w+(?<=ONLINE)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+',
    texto))

# Negative Lookbehind
pprint(re.findall(
    r'\w+(?<!ONLINE)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+',
    texto))
