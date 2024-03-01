n = int(input())
b = n - 1


for s in range(n + 1):
    for i in range(s):
        print('*', end='')
    print('')

for i in range(n -1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print('')



