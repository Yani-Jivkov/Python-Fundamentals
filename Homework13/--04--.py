# Peter:123:programming basics
# John:5622:fundamentals
# Maya:89:fundamentals
# Lilly:633:fundamentals
# fundamentals

my_dict = {}
my_dict1 = {}
while True:
    command = input()

    if ':' not in command:
        if command == 'programming_basics':
            for x in my_dict1.keys():
                if my_dict1[x] == ' '.join(command.split('_')):
                    print(f"{x} - {my_dict[x]}")
        else:
            for x in my_dict1.keys():
                if my_dict1[x] == command:
                    print(f"{x} - {my_dict[x]}")
        break

    student = command.split(':')

    for i in range(0, len(student), 3):
        my_dict[student[i]] = student[i + 1]
        my_dict1[student[i]] = student[i + 2]

