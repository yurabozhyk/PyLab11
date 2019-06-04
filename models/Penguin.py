from models.AquariumAnimal import AquariumAnimal
from models.SpeciesOfPenguin import SpeciesOfPenguin

class Penguin(AquariumAnimal):
    def __init__(self, name="", age=0, year_in_zoo=0, sex=None,
                 volume_of_aquarium=0, Species=None, height=0, weight=0,
                 SpeciesOfPenguin=None):
                 super().__init__(name, age, year_in_zoo, sex, volume_of_aquarium,
                                  Species)
                 self.height = height
                 self.weight = weight
                 self.SpeciesOfPenguin = SpeciesOfPenguin
