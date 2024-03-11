# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy

my_dict = {}

while True:
    input_data = input()

    if input_data == 'buy':
        break

    product, price, quantity = input_data.split()
    price = float(price)
    quantity = float(quantity)

    if product not in my_dict:
        my_dict[product] = [price, quantity]
    else:
        my_dict[product][1] += quantity
        my_dict[product][0] = price


for product, data in my_dict.items():
    total_price = data[0] * data[1]
    print(f'{product} -> {total_price:.2f}')

