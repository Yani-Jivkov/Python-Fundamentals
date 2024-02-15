electrons = int(input())
shells = []
while electrons > 0:
    shells.append(0)
    shell = shells.index(shells[-1]) + 1
    maxElectrons = 2 * shell**2
    shells.remove(0)
    shells.append(maxElectrons)
    electrons -= maxElectrons
    if electrons < 0:
        subtract = abs(electrons)
        shells[-1] -= subtract
print(shells)
