# Description: This file is the main file of the project. It reads the configuration file, gets the initial seed, creates the Game of Life object and starts the simulation.
from game_of_life import GameOfLife,read_configuration, get_initial_seed,start_simulation
import unit_tests
import unittest


def main() -> None:
    # Read configuration
    num_generations, initial_seed_name, oscillation_time, output_document, config = read_configuration("config.txt")

    # Get initial seed
    initial_seed = get_initial_seed(initial_seed_name, config)

    # Create the Game of Life object
    game = GameOfLife(initial_seed)
    

    # Start simulation
    start_simulation(game, num_generations, oscillation_time, output_document)

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(unit_tests)
    result = unittest.TextTestRunner().run(suite)

    # If the tests pass, run the main code
    if result.wasSuccessful():
        main()