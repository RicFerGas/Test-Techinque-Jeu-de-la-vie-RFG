import os
from typing import List, Tuple, Any
import time
from initial_seeds import seeds


class GameOfLife:
    def __init__(self, initial_grid: List[List[bool]]):
        # Initialize the grid
        self.grid = initial_grid
        # Set the grid dimensions
        self.GRID_HEIGHT = len(initial_grid)
        self.GRID_WIDTH = len(initial_grid[0])
        # Save the states of the game
        self.states = []
        self.states_count = 0
        #Save the initial state
        self.states.append(self.grid)


    def evolve(self):
        self.states_count += 1  
        new_grid = [[False] * self.GRID_WIDTH for _ in range(self.GRID_HEIGHT)]
        for i in range(self.GRID_HEIGHT):
            for j in range(self.GRID_WIDTH):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i][j] and live_neighbors in [2, 3]: # Any live cell with two or three live neighbors survives
                    new_grid[i][j] = True
                elif not self.grid[i][j] and live_neighbors == 3: # Any dead cell with three live neighbors becomes a live cell
                    new_grid[i][j] = True
                else:
                    new_grid[i][j] = False # All other live cells die in the next generation
        #Save the state
        self.states.append(new_grid)
        self.grid = new_grid # Update the grid

    def count_live_neighbors(self, i: int, j: int) -> int:
        count = 0
        for x in range(i - 1, i + 2): # Loop over the 3x3 neighborhood
            for y in range(j - 1, j + 2): # Loop over the 3x3 neighborhood
                if x == i and y == j: # Skip the current cell
                    continue
                if 0 <= x < self.GRID_HEIGHT and 0 <= y < self.GRID_WIDTH: # Check the boundaries
                    if self.grid[x][y]: # Check if the cell is alive
                        count += 1
        return count # Return the number of live neighbors

    def display_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print("Game of Life - Simulation")
        print(f"Generation: {self.states_count}")
        print("Press Ctrl+C to stop the simulation.")
        for row in self.grid:
            print("".join(["[o]" if cell else "[ ]" for cell in row])) # Display the grid
        print()

def write_game_states_to_file(output_document: str, game: GameOfLife) -> None:
    # Write the game states to a file in the "Runned games" folder
    with open('Runned games/'+output_document, "w") as file:
        for i, state in enumerate(game.states):
            file.write(f"Generation: {i}\n")
            for row in state:
                file.write("".join(["[o]" if cell else "[ ]" for cell in row]) + "\n")
            file.write("\n")

def read_configuration(filename: str):
    # Read the configuration file and return the parameters
    config: List[str] = []
    with open(filename, "r") as file:
        for line in file:
            line = line.split("#")[0].strip()
            if line: 
                config.append(line)
    num_generations: int = int(config[0].strip()) 
    initial_seed_name: str = config[1].strip().strip('"')
    oscillation_time: float = float(config[2].strip()) 
    output_document: str = config[3].strip()
    return num_generations, initial_seed_name, oscillation_time, output_document, config

def get_initial_seed(initial_seed_name: str, config: List[str]) -> List[List[int]]:
    # Determines the initial seed based on its name or custom seed content.
    custom_seed: List[List[int]] = []
    if initial_seed_name.startswith("Custom"):
        custom_seed_content: str = '\n'.join(config[4:]).strip() # Get the custom seed content as a string
        custom_seed = eval(custom_seed_content)  # Evaluate the content as Python code
        initial_seed_name = "Custom"
    if initial_seed_name in seeds:
        initial_seed = seeds[initial_seed_name] # Get the initial seed from the seeds dictionary
    elif custom_seed:
        initial_seed = custom_seed # Use the custom seed
    else:
        print("Error: Initial seed not found.")
        exit()
    return initial_seed

def start_simulation(game: GameOfLife, num_generations: int, oscillation_time: float, output_document: str) -> None:
    # Starts the simulation using the specified Game of Life object and parameters.
    game.display_grid() 
    print("Initial state:")
    ready = input("Press Enter to start the simulation")
    if ready == "":
        print("Simulation started")
        try:
            for _ in range(num_generations):
                game.evolve()
                # Display the game grid
                game.display_grid()
                time.sleep(oscillation_time)
        except KeyboardInterrupt:
            write_game_states_to_file(output_document, game)
            print("Simulation stopped by user. Run saved successfully.")
        write_game_states_to_file(output_document, game)
        print("Simulation completed. Run saved successfully.")
        exit()
    else:
        print("Invalid input. Exiting the simulation.")
        exit()
