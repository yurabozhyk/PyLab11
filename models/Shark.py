from models.AquariumAnimal import AquariumAnimal
from models.SpeciesOfSharks import SpeciesOfSharks
from models.SwimType import SwimType

class Shark(AquariumAnimal):
    def __init__(self, name="", age=0, year_in_zoo=0, sex=None,
                 volumeOfAquarium=0, Species=None, SpeciesOfSharks=None,
                 speed=0, SwimType=None):
                 super().__init__(name, age, year_in_zoo, sex, volumeOfAquarium,
                                  Species)
                 self.SpeciesOfSharks = SpeciesOfSharks
                 self.speed = speed
                 self.SwimType = SwimType
