def sort(a):
    new_list = []
    for k in a:
        new_list.append(k)
        new_list.sort()
    return new_list

nums = [int(i) for i in input().split()]

print(sort(nums))
