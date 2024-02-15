list_1 = input().split(', ')
list_2 = input().split(', ')
print_list = []
for i in list_1:
    for k in list_2:
        if i in k:
            if i in print_list:
                continue
            else:
                print_list.append(i)
print(print_list)
