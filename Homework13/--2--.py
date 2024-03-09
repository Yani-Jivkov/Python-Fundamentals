# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes

inputt = input().split()
inputt1 = input().split()
my_dict = {}
helper = False
for i in range(0, len(inputt), 2):
    my_dict[inputt[i]] = int(inputt[i + 1])
for y in inputt1:
    for x in my_dict.keys():
        if x == y:
            print(f'We have {my_dict[x]} of {x} left')
            helper = False
            break
        else:
            helper = True
    if helper:
        print(f'Sorry, we don\'t have {y}')
