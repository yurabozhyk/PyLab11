from models.AquariumAnimal import AquariumAnimal
from models.Shell import Shell

class Turtle(AquariumAnimal):
    def __init__(self, name="", age=0, year_in_zoo=0, sex=None,
                 volume_of_aquarium=0, Species=None, Shell=None,
                 immersion_depth=0):
                 super().__init__(name, age, year_in_zoo, sex, volume_of_aquarium,
                                  Species)
                 self.Shell = Shell
                 self.immersion_depth = immersion_depth
