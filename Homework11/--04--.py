class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            mammal = ', '.join(self.mammals)
            print(f'Mammals in {self.name}: {mammal}')
        elif species == 'fish':
            fishes = ', '.join(self.fishes)
            print(f'Fishes in {self.name}: {fishes}')
        else:
            bird = ', '.join(self.birds)
            print(f'Birds in {self.name}: {bird}')

        print(f'Total animals: {Zoo.__animals}')


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for i in range(n):
    animal_info = input().split()
    species = animal_info[0]
    animal = animal_info[1]
    zoo.add_animal(species, animal)

species = input()
zoo.get_info(species)

