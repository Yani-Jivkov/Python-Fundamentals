import re
data = input()
regex = r'\+359 [0-9] [0-9]{3} [0-9]{4}\b|\+359-[0-9]-[0-9]{3}-[0-9]{4}\b'
product = re.findall(regex, data)
print(', '.join(product))
