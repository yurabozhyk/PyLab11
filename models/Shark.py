from models.AquariumAnimal import AquariumAnimal
from models.SpeciesOfSharks import SpeciesOfSharks
from models.SwimType import SwimType

class Shark(AquariumAnimal):
    def __init__(self, name="", age=0, yearInZoo=0, sex=None,
                 volumeOfAquarium=0, Species=None, SpeciesOfSharks=None,
                 speed=0, SwimType=None):
                 super().__init__(name, age, yearInZoo, sex, volumeOfAquarium,
                                  Species)
                 self.SpeciesOfSharks = SpeciesOfSharks
                 self.speed = speed
                 self.SwimType = SwimType
