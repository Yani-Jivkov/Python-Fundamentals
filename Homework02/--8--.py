
coffee = 0

while True:
    event = input()

    if event == 'END':
        break

    if event == 'coding' or event == 'CODING':
        if event.isupper() == True:
            coffee += 2
        else:
            coffee += 1
    elif event == 'dog' or event == 'cat' or event == 'DOG' or event == 'CAT':
        if event.isupper() == True:
            coffee += 2
        else:
            coffee += 1
    elif event == 'movie' or event == 'MOVIE':
        if event.isupper() == True:
            coffee += 2
        else:
            coffee += 1
    else:
        continue
if coffee <= 5:
    print(coffee)
else:
    print('You need extra sleep')


