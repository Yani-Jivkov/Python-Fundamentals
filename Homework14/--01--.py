# text text text

word = input()
my_dict = {}

for i in range(len(word)):

    if word[i] not in my_dict.keys():
        my_dict[word[i]] = 1
    else:
        my_dict[word[i]] += 1

for i in my_dict.keys():
    if i == ' ':
        continue
    else:
        print(f'{i} -> {my_dict[i]}')
