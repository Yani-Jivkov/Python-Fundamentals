data = input().split()
multiply = 0

if len(data[0]) <= len(data[1]):
    for i in range(len(data[0])):
        multiply += ord(data[0][i]) * ord(data[1][i])

    if len(data[0]) < len(data[1]):
        for i in range(len(data[1]) - len(data[0])):
            multiply += ord(data[1][i + len(data[0])])
    print(multiply)

else:
    for i in range(len(data[1])):
        multiply += ord(data[1][i]) * ord(data[0][i])

    if len(data[1]) < len(data[0]):
        for i in range(len(data[0]) - len(data[1])):
            multiply += ord(data[0][i + len(data[1])])
    print(multiply)
