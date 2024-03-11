def odd_even_sum(a):
    odd_sum = 0
    even_sum = 0

    for i in range(len(a)):
        if int(num[i]) % 2 == 0:
            odd_sum += int(num[i])
        else:
            even_sum += int(num[i])

    print(f'Odd sum = {even_sum}, Even sum = {odd_sum}')

num = input()
odd_even_sum(num)
