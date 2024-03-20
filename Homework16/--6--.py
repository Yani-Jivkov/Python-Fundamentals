data = input()
new_word = ''
for i in range(len(data)):
    if i == 0:
        new_word += data[i]
        continue
    if data[i - 1] == data[i]:
        continue
    new_word += data[i]

print(new_word)