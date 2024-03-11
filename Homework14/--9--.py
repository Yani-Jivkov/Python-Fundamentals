# In
# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5

n = int(input())

my_dict = {}

for i in range(n):
    name = input()
    grade = float(input())
    listt = []

    if name in my_dict.keys():
        listt = my_dict[name]
        listt[0] += 1
        listt[1] += grade
        my_dict[name] = listt
    else:
        listt = [1, grade]
        my_dict[name] = listt


for x in my_dict.keys():
    if my_dict[x][1] / my_dict[x][0] >= 4.5:
        print(f'{x} -> {my_dict[x][1] / my_dict[x][0]:.2f}')
