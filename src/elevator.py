from turtle import distance, down
from typing import List, Optional

from elevator_request import ElevatorRequest


class Elevator:
    def __init__(self, id=1, speed=1):
        self.id = id
        self.speed = speed
        self.current_floor = 1
        self.current_direction = None
        self.current_destination = None
        self.stops: List[ElevatorRequest] = []

    def __update_destination(self):
        if not self.stops:
            self.current_destination = None
            self.current_direction = None
            return

        if self.current_direction == ElevatorRequest.DOWN:
            lowest_requested_floor = float("inf")
            for stop in self.stops:
                if stop.floor < lowest_requested_floor:
                    self.current_destination = stop.floor
                    lowest_requested_floor = stop.floor

        elif self.current_direction == ElevatorRequest.UP:
            highest_requested_floor = float("-inf")
            for stop in self.stops:
                if stop.floor > highest_requested_floor:
                    self.current_destination = stop.floor
                    highest_requested_floor = stop.floor

        else:
            self.current_destination = self.stops[0].floor
            self.current_direction = (
                ElevatorRequest.UP
                if self.stops[0].floor > self.current_floor
                else ElevatorRequest.DOWN
            )

    def add_request(self, floor: int, direction=None):
        self.stops.append(ElevatorRequest(floor, direction))
        self.__update_destination()

    def __stop_at_current_floor(self):
        stopped = False
        index = 0
        for i in range(len(self.stops)):
            stop = self.stops[index]
            if stop.floor == self.current_floor and (
                (stop.direction == self.current_direction or not stop.direction)
                or stop.floor == self.current_destination
            ):
                stopped = True
                self.stops.pop(index)
            else:
                index += 1

        if self.current_destination == self.current_floor:
            self.current_direction = None
            self.__update_destination()

        if stopped:
            print("Elevator stopped at floor " + str(self.current_floor))

        return stopped

    def move_elevator(self) -> Optional[int]:
        if not self.current_destination:
            return

        if self.__stop_at_current_floor():
            return

        if self.current_direction == ElevatorRequest.DOWN:
            self.current_floor -= self.speed
        else:
            self.current_floor += self.speed
