import re
data = input()
regex = r'[0-9]{2}\/[A-Z][a-z]{2}\/[0-9]{4}|[0-9]{2}\-[A-Z][a-z]{2}-[0-9]{4}|[0-9]{2}\.[A-Z][a-z]{2}\.[0-9]{4}'
product = re.findall(regex, data)

for i in product:
    daa = i.split(i[2])
    print(f'Day: {daa[0]}, Month: {daa[1]}, Year: {daa[2]}')