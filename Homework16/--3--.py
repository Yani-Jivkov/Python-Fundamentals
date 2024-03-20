data = input().split('\\')
place = data[len(data) - 1].split('.')
print(f'\nFile name: {place[0]} \nFile extension: {place[1]}')