numbers = input()
n_to_remove = int(input())

numbers = [int(number) for number in numbers.split()]

smallest_numbers = sorted(numbers)[:n_to_remove]

for num in smallest_numbers:
    numbers.remove(num)

print(', '.join(str(number) for number in numbers))
