class Weapon:
    bullets = 0
    def __init__(self, bullets):
        Weapon.bullets = bullets

    def shoot(self):
        if Weapon.bullets > 0:
            Weapon.bullets -= 1
            return f'shooting...'
        else:
            return f'no bullets left'

    def __repr__(self):
        return f'Remaining bullets: {Weapon.bullets}'

# Example
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
