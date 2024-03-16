text = input()
let = ''
dig = ''
oth = ''
for char in text:
    if char.isidentifier():
        let += char
    elif char.isdecimal():
        dig += char
    else:
        oth += char

print(dig)
print(let)
print(oth)
