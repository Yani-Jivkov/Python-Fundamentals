main_list = [int(n) for n in input().split(", ")]
even_list = []

for index, number in enumerate(main_list):
    if number % 2 == 0:
        even_list.append(index)

print(even_list)
