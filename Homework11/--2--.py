class Party:
    def __init__(self):
        self.people = []

party = Party()

while True:
    lines = input()

    if lines == 'End':
        pp = ', '.join(party.people)
        print(f'Going: {pp}')
        print(f'Total: {len(party.people)}')
        break

    party.people.append(lines)
