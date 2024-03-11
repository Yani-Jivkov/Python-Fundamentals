# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

n = int(input())
my_dict = {}

for i in range(n):
    data = input().split()

    if data[0] == 'register':
        if data[1] in my_dict.keys():
            print(f'ERROR: already registered with plate number {data[2]}')
        else:
            my_dict[data[1]] = data[2]
            print(f'{data[1]} registered {data[2]} successfully')

    else:
        if data[1] not in my_dict.keys():
            print(f'ERROR: user {data[1]} not found')
        else:
            del my_dict[data[1]]
            print(f'{data[1]} unregistered successfully')

for x in my_dict.keys():
    print(f'{x} => {my_dict[x]}')
