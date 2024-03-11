import string

def valid_password_check(a):
    list4e = []
    helper1 = 0
    helper2 = 0
    if len(a) < 6:
        print(f'Password must be between 6 and 10 characters')
        helper1 += 1
    lower = list(string.ascii_letters)
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for k in range(len(a)):
        if a[k] in lower or a[k] in nums:
            continue
        else:
            helper2 += 1
            helper1 += 1
            if helper2 == 1:
                print(f'Password must consist only of letters and digits')
    for i in a:
        if i in nums:
            list4e.append(i)
    if len(list4e) < 2:
        print(f'Password must have at least 2 digits')
        helper1 += 1
    if helper1 < 1:
        print(f'Password is valid')

password = input()
valid_password_check(password)
