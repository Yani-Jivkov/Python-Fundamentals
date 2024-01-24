n = int(input())
magic_word = input()
main_list = []
magic_list = []
for i in range(n):
    string = input()

    if magic_word in string:
        magic_list.append(string)

    main_list.append(string)

print(main_list)
print(magic_list)
