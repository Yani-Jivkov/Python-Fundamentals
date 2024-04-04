import re
pattern = r'>>([A-Za-z]+)<<(\d+.?\d+)\!(\d+)'
bought_furniture = []
total_price = []
while True:
    data = input()
    if data == 'Purchase':
        break
    matches = re.findall(pattern, data)
    if matches:
        bought_furniture.append(matches[0][0])
        total_price.append([matches[0][1], matches[0][2]])
print(f'Bought furniture:')
for i in bought_furniture:
    print(i)
total_sums = 0
for i in total_price:
    total_sums += float(i[0]) * float(i[1])
print(f'Total money spend: {total_sums:.2f}')