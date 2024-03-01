input_str = input()
input_numbers = list(map(int, input_str.split(', ')))

groups = {}

for num in input_numbers:
    key = ((num - 1) // 10 + 1) * 10
    if key in groups:
        groups[key].append(num)
    else:
        groups[key] = [num]

max_group = max(groups.keys()) if groups else 0

for group in range(10, max_group + 1, 10):
    if group in groups or group <= max_group:
        print(f"Group of {group}'s: {groups.get(group, [])}")
