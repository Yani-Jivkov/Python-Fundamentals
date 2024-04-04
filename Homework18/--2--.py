import re
data = input()
pattern = r'\b_[A-Za-z]+\b'
matches = re.findall(pattern, data)
print_list = []
for i in matches:
    helper = []
    helper1 = 0
    for x in i:
        helper1 += 1
        if helper1 == 1:
            continue
        helper.append(x)
    print_list.append(''.join(helper))
print(','.join(print_list))