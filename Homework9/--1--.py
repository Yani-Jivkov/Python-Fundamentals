string = input()

x = [i for i in string if i.lower() not in ['a', 'e', 'i', 'o', 'u']]
print(''.join(x))
