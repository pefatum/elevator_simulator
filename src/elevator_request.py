class ElevatorRequest:
    UP = "up"
    DOWN = "down"
    valid_directions = [UP, DOWN]

    def __init__(self, floor, direction=None):
        self.floor = floor
        self.direction = direction
