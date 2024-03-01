employees_happiness = [int(n) for n in input().split()]
improvement = int(input())
happy_count = 0
avg_happy = 0
for i in range(len(employees_happiness)):
    employees_happiness[i] *= 3
    avg_happy += employees_happiness[i]

avg_happy = avg_happy / len(employees_happiness)

for k in employees_happiness:
    if k >= avg_happy:
        happy_count += 1


if happy_count >= len(employees_happiness) / 2:
    print(f'Score: {happy_count}/{len(employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{len(employees_happiness)}. Employees are not happy!')
