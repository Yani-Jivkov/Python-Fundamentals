input_list = input()

list = input_list.split()

for i in range(len(list)):
    add = int(list[i]) * -1

    list.pop(i)
    list.insert(i, add)

print(list)
