from typing import List

from elevator_request import ElevatorRequest


class Elevator:
    def __init__(self, id=1, speed=1):
        self.id = id
        self.speed = speed
        self.current_floor = 1
        self.current_direction = None
        self.current_destination = None
        self.stops: List[ElevatorRequest] = []
    
    def __get_number_of_higher_stops(self):
        num_stops = 0
        for stop in self.stops:
            if stop.floor > self.current_floor:
                num_stops += 1
        return num_stops

    def __get_number_of_lower_stops(self):
        num_stops = 0
        for stop in self.stops:
            if stop.floor < self.current_floor:
                num_stops += 1
        return num_stops

    def __calculate_highest_floor(self):
        highest_requested_floor = float("-inf")
        for stop in self.stops:
            if stop.floor > highest_requested_floor:
                highest_requested_floor = stop.floor
        return highest_requested_floor
    
    def __calculate_lowest_floor(self):
        lowest_requested_floor = float("inf")
        for stop in self.stops:
            if stop.floor < lowest_requested_floor:
                lowest_requested_floor = stop.floor
        return lowest_requested_floor

    def __update_elevator_goal(self):
        if not self.stops:
            self.current_destination = None
            self.current_direction = None
            return
        elif not self.current_direction:
            self.current_direction = (
                ElevatorRequest.UP
                if self.stops[0].floor > self.current_floor
                else ElevatorRequest.DOWN
            )
        else:
            if self.current_direction == ElevatorRequest.DOWN and self.__get_number_of_lower_stops() == 0:
                self.current_direction = ElevatorRequest.UP
            elif self.current_direction == ElevatorRequest.UP and self.__get_number_of_higher_stops() == 0:
                self.current_direction = ElevatorRequest.DOWN

        if self.current_direction == ElevatorRequest.DOWN:
            self.current_destination = self.__calculate_lowest_floor()

        elif self.current_direction == ElevatorRequest.UP:
            self.current_destination = self.__calculate_highest_floor()

    def add_request(self, floor: int, direction=None):
        self.stops.append(ElevatorRequest(floor, direction))

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

        if stopped:
            print("Elevator stopped at floor " + str(self.current_floor))

        return stopped

    def move_elevator(self):
        if self.__stop_at_current_floor():
            return

        self.__update_elevator_goal()

        if not self.current_destination:
            return

        if self.current_direction == ElevatorRequest.DOWN:
            self.current_floor -= self.speed
        else:
            self.current_floor += self.speed
