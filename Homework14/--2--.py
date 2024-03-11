# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop

my_dict = {}

while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())


    if resource not in my_dict.keys():
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity

for i in my_dict.keys():
    print(f'{i} -> {my_dict[i]}')


