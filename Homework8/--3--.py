def printa_to_b(a, b):
    for i in range(a + 1, b):
        print(chr(i), end=' ')

str_1 = input()
str_2 = input()

str_1 = ord(str_1)
str_2 = ord(str_2)

printa_to_b(str_1, str_2)
