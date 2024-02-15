rooms = int(input())
chairs_left = 0
counter = 0
for i in range(rooms):
    input_1 = input().split()

    chairs = len(input_1[0])
    people = int(input_1[1])

    if chairs >= people:
        chairs_left += chairs - people
    else:
        counter += 1
        print(f'{people - chairs} more chairs needed in room {i + 1}')

if counter == 0:
    print(f'Game On, {chairs_left} free chairs left')
