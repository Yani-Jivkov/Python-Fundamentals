
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']

triples = int(input())

for i in range(0, triples):
    letter1 = characters[i]
    for k in range(0, triples):
        letter2 = characters[k]
        for l in range(0, triples):
            letter3 = characters[l]
            print(f'{letter1}{letter2}{letter3}')
