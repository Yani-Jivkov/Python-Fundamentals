list = [0] * 10

while True:
    notes = input()

    if notes == 'End':
        main_list = [i for i in list if i != 0]
        print(main_list)
        break
    else:
        importance, note = notes.split('-')
        list[int(importance) - 1] = note

