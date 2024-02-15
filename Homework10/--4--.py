list_1 = list(map(int, input().split(', ')))

positive_num = []
negative_num = []
even_num = []
odd_num = []

for i in list_1:
    if i >= 0:
        positive_num.append(i)

for k in list_1:
    if k < 0:
        negative_num.append(k)

for l in list_1:
    if l % 2 == 0:
        even_num.append(l)

for m in list_1:
    if m % 2 != 0:
        odd_num.append(m)

positive_num = list(map(str, positive_num))
positive_num = ', '.join(positive_num)
negative_num = list(map(str, negative_num))
negative_num = ', '.join(negative_num)
even_num = list(map(str, even_num))
even_num = ', '.join(even_num)
odd_num = list(map(str, odd_num))
odd_num = ', '.join(odd_num)

print(f'Positive: {positive_num}')
print(f'Negative: {negative_num}')
print(f'Even: {even_num}')
print(f'Odd: {odd_num}')
