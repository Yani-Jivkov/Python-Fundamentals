# bread 10 butter 4 sugar 9 jam 12

inputt = input().split()
my_dict = {}
for i in range(0, len(inputt), 2):
    my_dict[inputt[i]] = int(inputt[i + 1])
print(f'{my_dict}')
