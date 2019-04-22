class ZooManager:
    def __init__(self, list_of_aquarium_animal = None):
        self.list_of_aquarium_animal = list_of_aquarium_animal

    def sort_by_species_of_animal(self, Species, reverse = False):
        return sorted(self.list_of_aquarium_animal, key = lambda aquarium_animal: aquarium_animal.Species.value, reverse = reverse)

    def sort_by_volume_of_aquarium(self, volume_of_aquarium, reverse = False):
        return sorted(self.list_of_aquarium_animal, key = lambda aquarium_animal: aquarium_animal.volume_of_aquarium, reverse = reverse)

    def find_aquarium_animal_older_than(self, years):
        return list(filter(lambda aquarium_animal: aquarium_animal.age > years, self.list_of_aquarium_animal))
