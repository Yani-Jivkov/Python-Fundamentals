def palindromes(a):
    for i in a:
        if str(i) == str(i)[::-1]:
            print(f'True')
        else:
            print(f'False')

nums = [int(k) for k in input().split(', ')]

palindromes(nums)
