data = input().split()
list_sum = []
for word in data:
    for i in range(len(word)):
        list_sum.append(word)
print(''.join(list_sum))
