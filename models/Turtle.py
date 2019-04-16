from models.AquariumAnimal import AquariumAnimal
from models.Shell import Shell

class Turtle(AquariumAnimal):
    def __init__(self, name="", age=0, yearInZoo=0, sex=None,
                 volumeOfAquarium=0, Species=None, Shell=None,
                 immersionDepth=0):
                 super().__init__(name, age, yearInZoo, sex, volumeOfAquarium,
                                  Species)
                 self.Shell = Shell
                 self.immersionDepth = immersionDepth
