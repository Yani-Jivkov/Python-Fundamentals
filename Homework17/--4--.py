import re
regex = r'(^|(?<=\s))-?([0]|[1-9][1-9]*)(\.\d+)?($|(?=\s))'
data = input()
product = re.findall(regex, data)

for i in product:
    print(''.join(i), sep=' ')