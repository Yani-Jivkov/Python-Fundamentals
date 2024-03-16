dict_words = {}
while True:
    data = input()
    if data == 'end':
        break
    dict_words[data] = data[::-1]
    print(f'{data} = {dict_words[data]}')

