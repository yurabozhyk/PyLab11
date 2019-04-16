class ZooManager:
    def __init__(self, listOfAquariumAnimal = None):
        self.listOfAquariumAnimal = listOfAquariumAnimal

    def sortBySpeciesOfAnimal(self, Species, reverse = False):
        return sorted(self.listOfAquariumAnimal, key = lambda aquariumAnimal: aquariumAnimal.Species.value, reverse = reverse)

    def sortByVolumeOfAquarium(self, volumeOfAquarium, reverse = False):
        return sorted(self.listOfAquariumAnimal, key = lambda aquariumAnimal: aquariumAnimal.volumeOfAquarium, reverse = reverse)

    def findAquariumAnimalsOlderThan(self, years):
        return list(filter(lambda aquariumAnimal: aquariumAnimal.age > years, self.listOfAquariumAnimal))
