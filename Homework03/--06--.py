year = int(input())

while True:
    year += 1

    helper = str(year)
    if len(helper) == 3:
        if helper[0] == helper[1] or helper[0] == helper[2]:
            continue
        elif helper[1] == helper[0] or helper[1] == helper[2]:
            continue
        elif helper[2] == helper[0] or helper[2] == helper[1]:
            continue
        else:
            print(helper)
            break
    elif len(helper) == 4:
        if helper[0] == helper[1] or helper[0] == helper[2] or helper[0] == helper[3]:
            continue
        elif helper[1] == helper[0] or helper[1] == helper[2] or helper[1] == helper[3]:
            continue
        elif helper[2] == helper[0] or helper[2] == helper[1] or helper[2] == helper[3]:
            continue
        elif helper[3] == helper[0] or helper[3] == helper[1] or helper[3] == helper[2]:
            continue
        else:
            print(helper)
            break
    elif len(helper) == 5:
        if helper[0] == helper[1] or helper[0] == helper[2] or helper[0] == helper[3] or helper[0] == helper[4]:
            continue
        elif helper[1] == helper[0] or helper[1] == helper[2] or helper[1] == helper[3] or helper[1] == helper[4]:
            continue
        elif helper[2] == helper[0] or helper[2] == helper[1] or helper[2] == helper[3] or helper[2] == helper[4]:
            continue
        elif helper[3] == helper[0] or helper[3] == helper[1] or helper[3] == helper[2] or helper[3] == helper[4]:
            continue
        elif helper[4] == helper[0] or helper[4] == helper[1] or helper[4] == helper[2] or helper[4] == helper[3]:
            continue
        else:
            print(helper)
            break
