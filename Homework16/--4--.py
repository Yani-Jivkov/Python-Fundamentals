data = input()
new_word = ''
for i in data:
    new_word += chr(ord(i) + 3)
print(new_word)