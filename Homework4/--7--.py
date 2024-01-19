capacity = 255
total_liters = 0

n = int(input())
for _ in range(n):
    liters = int(input())

    if total_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters

print(total_liters)
