class Building:

    def __init__(self, floors=10):
        self.floors = floors

    def is_valid_floor(self, floor: int):
        return floor <= self.floors and floor > 0