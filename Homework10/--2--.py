list_1 = list(map(int, input().split('.')))

list_1[2] += 1
if list_1[2] == 10:
    list_1[2] = 0
    list_1[1] += 1
    if list_1[1] == 10:
        list_1[1] = 0
        list_1[0] += 1


list_1 = list(map(str, list_1))
resultString = '.'.join(list_1)
print(resultString)
