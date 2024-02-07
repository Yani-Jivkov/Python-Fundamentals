
def sum_numbers(a, b):
    result = a + b
    return result

def subtract(result, b):
    return result - b

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = sum_numbers(num_1, num_2)
print(subtract(result, num_3))
