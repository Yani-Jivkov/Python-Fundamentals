n = int(input())

for _ in range(n):
    word = input()
    for i in range(len(word)):
        if word[i] != ',' and word[i] != '.' and word[i] != '_':
            pure_word = True
        else:
            pure_word = False
            break
    if pure_word == True:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
