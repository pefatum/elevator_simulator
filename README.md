# Elevator Simulator
This is a program that simulates an elevator in a building

## How To Run
1. Install Python 3
2. Clone this github repository locally
3. To begin the program, navigate to the /src folder and run `py cli.py`
4. Follow the prompts on the simulation
    1. If you want to simulate calling the elevator (pushing the up/down button), select option 1. Enter the floor and desired direction for the request
    2. If you want to simulate pressing a button inside the elevator, select option 2. Enter the floor for the request
    3. If you want to continue the simulation, press option 3
    4. If you want to exit the simulator, press option 4

## Elevator Algorithm
Here is how the elevator decides which floor to go to:
1. If the elevator is not heading in any direction and has no stops requested, it will remain idle
2. If the elevator is not heading in any direction and has stops requested, it will head in the direction of the oldest request
3. The elevator will continue in its current direction until it reaches the last floor in that direction (highest or lowest)
4. Once it has reached the final floor in a certain direction, it will head in the opposite direction if there are any requests the other way
5. Otherwise, it will remain idle

## Assumptions
1. Passengers do not want to get on an elevator going in the other direction
2. It takes one unit of time for the elevator to stop at a floor and let passengers off or on. Passengers are given that unit of time to select a floor when getting on the elevator
3. If two commands are entered during the same unit of time and the elevator does not already have a direction, the command entered first will be favored 
