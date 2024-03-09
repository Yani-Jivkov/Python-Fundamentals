# a, b, c, a
ASCII_Values = input().split(', ')
my_dict = {}

for i in range(len(ASCII_Values)):
    for x in my_dict.keys():
        if x == ASCII_Values[i]:
            break
    else:
        my_dict[ASCII_Values[i]] = ord(ASCII_Values[i])

print(my_dict)
