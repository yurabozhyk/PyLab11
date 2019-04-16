from models.AquariumAnimal import AquariumAnimal
from models.Penguin import Penguin
from models.Sex import Sex
from models.Shark import Shark
from models.Shell import Shell
from models.Species import Species
from models.SpeciesOfPenguin import SpeciesOfPenguin
from models.SpeciesOfSharks import SpeciesOfSharks
from models.SwimType import SwimType
from models.Turtle import Turtle
from managers.ZooManager import ZooManager

turtle = Turtle("Bobo", 140, 3, Sex.MALE, 400, Species.REPTILE)
shark = Shark("Lilo", 20, 5, Sex.FEMALE, 1000, Species.FISH)
penguin = Penguin("Fed", 7, 2, Sex.MALE, 600, Species.BIRDS)

listOfAquariumAnimal = [turtle, shark, penguin]
manager = ZooManager(listOfAquariumAnimal)

print(manager.sortBySpeciesOfAnimal(listOfAquariumAnimal))
print(manager.sortByVolumeOfAquarium(listOfAquariumAnimal))
print(manager.findAquariumAnimalsOlderThan(10))
