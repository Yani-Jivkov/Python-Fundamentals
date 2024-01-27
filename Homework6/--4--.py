money = [int(x) for x in input().split(', ')]
n = int(input())
sums = [0] * n

for i, num in enumerate(money):
    sums[i % n] += num

print(sums)
