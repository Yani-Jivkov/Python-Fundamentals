# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end

my_dict = {}
helper = []
while True:
    data = input()

    if data == 'end':
        break

    data = data.split(' : ')

    if data[1] not in my_dict.keys():
        my_dict[data[1]] = data[0]


for i in my_dict.keys():
    course_count = 0
    course_dict = {}
    list_help = []
    for x in my_dict.keys():
        if my_dict[x] == my_dict[i]:
            course_count += 1
            list_help.append(f'-- {x}')
            course_dict[my_dict[x]] = list_help


    for y in course_dict.keys():
        if y not in helper:
            print(f'{y}: {course_count}')
            print('\n'.join(course_dict[y]))
        helper.append(y)


