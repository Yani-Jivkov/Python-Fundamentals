from math import floor
centuries = int(input())

days = floor((centuries * 100) * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {centuries * 100:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes')
