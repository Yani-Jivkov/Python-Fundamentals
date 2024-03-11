deli = int(input())
grni = int(input())

for i in range(grni, deli, - 1):
    if i % deli == 0:
        print(i)
        break
