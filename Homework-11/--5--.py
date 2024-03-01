class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diametrer = diameter

    def calculate_circumference(self):
        return self.diametrer * Circle.__pi

    def calculate_area(self):
        return ((self.diametrer / 2) * (self.diametrer / 2)) * Circle.__pi

    def calculate_area_of_sector(self, angle):
        area = ((self.diametrer / 2) * (self.diametrer / 2)) * Circle.__pi
        return angle / (360 / area)

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
