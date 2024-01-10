st = int(input())
nd = int(input())
th = int(input())

if st > nd and st > th:
    print(st)
elif nd > st and nd > th:
    print(nd)
else:
    print(th)
