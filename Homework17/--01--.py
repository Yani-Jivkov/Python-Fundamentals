import re
data = input()
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
product = re.findall(regex, data)
print(' '.join(product))
