import enum


class CarType(enum.Enum):
    Sedan = 'Sedan'
    Coupe = 'Coupe'
    Crossover = 'Crossover'
    Hatchback = 'Hatchback'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)