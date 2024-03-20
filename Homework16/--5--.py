text = input()

emoticons = []
for i in range(len(text)):
    if text[i] == ':' and i + 1 < len(text):
        emoticons.append(text[i:i + 2])

for emoticon in emoticons:
    print(emoticon)
