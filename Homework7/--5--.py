def orders(order, times):
    if order == 'coffee':
        return times * 1.50
    elif order == 'water':
        return times * 1.00
    elif order == 'coke':
        return times * 1.40
    elif order == 'snacks':
        return times * 2.00


order = input()
n = int(input())

print(f'{orders(order, n):.2f}')
