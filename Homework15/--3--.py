pattern = input().strip()
text = input().strip()

while pattern in text:
    text = text.replace(pattern, '')

print(text)
