gifts = [x for x in input().split()]
while True:
    command = input()

    if command == 'No Money':
        break

    command = [k for k in command.split()]
    if command[0] == 'OutOfStock':

        for i in gifts:
            if (i == command[1]):
                place = gifts.index(command[1])
                gifts.pop(place)

    elif command[0] == 'Required':

         place = int(command[2])
         gifts.pop(place - 1)
         gifts.insert((place - 1), command[1])

    elif command[0] == 'JustInCase':
        gifts.pop(-1)
        gifts.append(command[1])

print(' '.join(gifts))

