from enum import Enum


class FarmAnimal(Enum):
    SHEEP = ((0,0), (0,1), (0,2), (0,3))
    PIG = ((0,0), (1,0), (0,1), (1,1))
    RABBIT = ((0,0), (1,0), (2,0), (3,0))
    HORSE = ((0,0), (1,0), (2,0))
    COW = ((0,0), (0,1), (0,2))
    UNICORN = ((0,0), (1,1), (1,2))

    def __str__(self):
        return self.name.capitalize()

class OutbackAnimal(Enum):
    KANGAROO = ((0,0), (1,1), (2,2), (3,3))
    PLATYPUS = ((0,0), (0,1), (1,1), (1,2))
    CROCODILE = ((0,0), (0,1), (0,2), (0,3))
    KOALA = ((0,0), (0,1), (1,1))
    COCKATOO = ((0,0), (1,1), (2,1))
    TIDALICK = ((1,0), (0,1), (1,2))

    def __str__(self):
        return self.name.capitalize()

class SavannahAnimal(Enum):
    GIRAFFE = ((0,0), (1,0), (2,0), (3,0))
    ZEBRA = ((1,0), (0,1), (1,2), (2,1))
    HIPPO = ((0,0), (0,2), (2,0), (2,2))
    ELEPHANT = ((0,0), (1,0), (0,1))
    LION = ((0,0), (0,1), (0,2))
    GRYPHON = ((0,0), (1,1), (0,2))

    def __str__(self):
        return self.name.capitalize()

# class OutbackAnimal(Enum):

REGIONS = {
    "FARM": FarmAnimal,
    "OUTBACK": OutbackAnimal,
    "SAVANNAH": SavannahAnimal
}


