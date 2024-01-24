n = int(input())
main_list = []
edited_list = []
for _ in range(n):
    num = int(input())

    main_list.append(num)

command = input()

if command == 'even':
    for i in range(n):
        if main_list[i] % 2 == 0:
            edited_list.append(main_list[i])
elif command == 'odd':
        for k in range(n):
            if main_list[k] % 2 != 0:
                edited_list.append(main_list[k])
elif command == 'negative':
        for l in range(n):
            if main_list[l] < 0:
                edited_list.append(main_list[l])
elif command == 'positive':
        for m in range(n):
            if main_list[m] >= 0:
                edited_list.append(main_list[m])

print(edited_list)

