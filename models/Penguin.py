from models.AquariumAnimal import AquariumAnimal
from models.SpeciesOfPenguin import SpeciesOfPenguin

class Penguin(AquariumAnimal):
    def __init__(self, name="", age=0, yearInZoo=0, sex=None,
                 volumeOfAquarium=0, Species=None, height=0, weight=0,
                 SpeciesOfPenguin=None):
                 super().__init__(name, age, yearInZoo, sex, volumeOfAquarium,
                                  Species)
                 self.height = height
                 self.weight = height
                 self.SpeciesOfPenguin = SpeciesOfPenguin
