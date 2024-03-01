n = int(input())

for i in range(1, n + 1):
    num = str(i)
    if len(num) == 2:
        if int(num[0]) + int(num[1]) == 5 or int(num[0]) + int(num[1]) == 7 or int(num[0]) + int(num[1]) == 11:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')
    else:
        if int(num[0]) == 5 or int(num[0]) == 7 or int(num[0]) == 11:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')
