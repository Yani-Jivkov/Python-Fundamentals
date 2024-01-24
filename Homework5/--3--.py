n = int(input())
count_of_pos = 0
sum_of_neg = 0
list_pos = []
list_neg = []
for i in range(n):
    num = int(input())

    if num >= 0:
        count_of_pos += 1
        list_pos.append(num)
    else:
      sum_of_neg += num
      list_neg.append(num)

print(list_pos)
print(list_neg)
print(f'Count of positives: {count_of_pos}')
print(f'Sum of negatives: {sum_of_neg}')

