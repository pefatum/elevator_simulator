from building import Building
from elevator import Elevator
from elevator_request import ElevatorRequest

menu_options = {
    1: "Call Elevator",
    2: "Enter Floor",
    3: "Proceed",
    4: "Exit",
}


def print_menu():
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def print_status(elevator: Elevator):
    print(
        "Elevator " + str(elevator.id) + " is at floor " + str(elevator.current_floor)
    )


def call_elevator(building: Building, elevator: Elevator):
    try:
        floor = int(input(f"Enter which floor you are on [1-{building.floors}]: "))
        if not building.is_valid_floor(floor):
            raise ValueError

        direction = input("Enter which direction you would like to go [up/down]: ")
        if direction not in ElevatorRequest.valid_directions:
            raise ValueError

        elevator.add_request(floor, direction)
    except ValueError:
        print("Invalid request entered.")


def enter_floor(building: Building, elevator: Elevator):
    try:
        floor = int(
            input(f"Enter which floor you would like to go to [1-{building.floors}]: ")
        )
        if not building.is_valid_floor(floor):
            raise ValueError
        elevator.add_request(floor)
    except ValueError:
        print("Invalid floor entered.")


def proceed(elevator: Elevator):
    floor = elevator.move_elevator()
    if floor:
        print("Elevator stopped at floor " + str(floor))


def simulator():
    elevator = Elevator()
    building = Building()

    while True:
        print_status(elevator)
        print_menu()
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                call_elevator(building, elevator)
            elif option == 2:
                enter_floor(building, elevator)
            elif option == 3:
                proceed(elevator)
            elif option == 4:
                print("Thanks for elevating!")
                exit()
            else:
                print("Please input a valid option.")
        except ValueError:
            print("Please input a valid option.")


if __name__ == "__main__":
    simulator()
