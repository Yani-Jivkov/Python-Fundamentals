# Adam-0888080808
# 2
# Mery
# Adam

my_dict = {}

while True:
    command = input()

    if '-' in command:
        name_num = command.split('-')

        my_dict[name_num[0]] = name_num[1]
    else:
        break

for i in range(int(command)):
    name = input()
    if name not in my_dict.keys():
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {my_dict[name]}')
