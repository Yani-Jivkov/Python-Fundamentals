import re
data = input()
pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
matches = re.findall(pattern, data)
for i in matches:
    print(i[0])