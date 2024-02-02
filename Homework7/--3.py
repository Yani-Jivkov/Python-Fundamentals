def calculator(function, num_1, num_2):
    if function == 'multiply':
        return num_1 * num_2
    elif function == 'divide':
        return num_1 / num_2
    elif function == 'add':
        return num_1 + num_2
    elif function == 'subtract':
        return num_1 - num_2


function = input()
num_1 = int(input())
num_2 = int(input())

print(int(calculator(function, num_1, num_2)))
