# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London

country = input().split(', ')
capital_city = input().split(', ')

for i in zip(country, capital_city):
    print(f'{i[0]} -> {i[1]}')
