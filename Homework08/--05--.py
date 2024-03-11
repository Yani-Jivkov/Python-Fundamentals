def even_print(a):
    new_list = []
    for k in range(len(a)):
        if a[k] % 2 == 0:
            new_list.append(a[k])
    return new_list

nums = [int(i) for i in input().split()]

print(even_print(nums))
