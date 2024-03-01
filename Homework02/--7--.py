
while True:
    new_string = ''
    word = input()

    if word == 'End':
        break

    if word == 'SoftUni':
        continue

    for i in range(len(word)):
        new_string += word[i]
        new_string += word[i]

    print(new_string)
