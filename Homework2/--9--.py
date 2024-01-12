

while True:
    name = input()

    if name == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        break

    if name == 'Voldemort':
        print(f'You must not speak of that name!')
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")


