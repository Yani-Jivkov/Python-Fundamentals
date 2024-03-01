wagon_count = int(input())

train = [0] * wagon_count

while True:
    command = input().split()

    if command[0] == "End":
        break

    action = command[0]
    if action == "add":
        people = int(c  and[1])
        train[-1] += people
    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)
