names_list = input().split(', ')
sort_list = sorted(names_list, key=lambda x: (-len(x), x))
print(sort_list)
