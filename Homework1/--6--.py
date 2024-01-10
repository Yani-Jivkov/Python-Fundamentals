budget = int(input())
total = 0
while True:
    money = input()

    if money == 'End':
        print(f'You bought everything needed.')
        break

    money = int(money)
    total += money

    if total > budget:
        print(f'You went in overdraft!')
        break
else:
    print(f'You bought everything needed.')
