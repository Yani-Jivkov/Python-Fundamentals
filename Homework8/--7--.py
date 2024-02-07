def min_max_sum(a):
    smalles_num = min(a)
    biggest_num = max(a)
    sum_of_all = sum(a)

    print(f'The minimum number is {smalles_num}')
    print(f'The maximum number is {biggest_num}')
    print(f'The sum number is: {sum_of_all}')



nums = [int(i) for i in input().split()]
min_max_sum(nums)
