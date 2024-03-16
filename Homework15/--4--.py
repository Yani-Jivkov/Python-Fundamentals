pattern = input().split(', ')
text = input()


for word in pattern:
    while word in text:
        text = text.replace(word, '*' * len(word))

# text = text.replace(pattern, '')

print(text)
