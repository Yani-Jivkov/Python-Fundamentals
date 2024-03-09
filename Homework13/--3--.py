# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics

my_dict = {}
total_products = 0
total_quantity = 0
while True:
    command = input()

    if command == 'statistics':
        break

    product = command.split(': ')

    for x in my_dict.keys():
        if x == product[0]:
            my_dict[product[0]] += int(product[1])
            break
    else:
        my_dict[product[0]] = int(product[1])

print(f'Products in stock:')
for i in my_dict.keys():
    print(f'{i}: {my_dict[i]}')
    total_products += 1
    total_quantity += my_dict[i]

print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')
