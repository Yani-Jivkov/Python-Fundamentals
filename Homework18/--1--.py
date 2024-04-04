import re
listt = []
pattern = r'\d+'
data = input()
while data:
    matches = re.findall(pattern, data)
    for i in matches:
        listt.append(i)
    data = input()
print(' '.join(listt))