import unittest
from typing import List, Tuple, Any
from game_of_life import GameOfLife, read_configuration, get_initial_seed
from initial_seeds import seeds

class TestGameOfLife(unittest.TestCase):
    def test_evolve(self):
        initial_grid: List[List[bool]] = [[False, True, False], [False, True, False], [False, True, False]]
        game = GameOfLife(initial_grid)
        game.evolve()
        expected_grid: List[List[bool]] = [[False, False, False], [True, True, True], [False, False, False]]
        self.assertEqual(game.grid, expected_grid)

    def test_count_live_neighbors(self):
        initial_grid: List[List[bool]] = [[False, True, False], [False, True, False], [False, True, False]]
        game = GameOfLife(initial_grid)
        self.assertEqual(game.count_live_neighbors(1, 1), 2)

class TestReadConfiguration(unittest.TestCase):
    def test_read_configuration(self):
        num_generations, initial_seed_name, oscillation_time, output_document, config = read_configuration("config.txt")
        self.assertIsInstance(num_generations, int)
        self.assertIsInstance(initial_seed_name, str)
        self.assertIsInstance(oscillation_time, float)
        self.assertIsInstance(output_document, str)
        self.assertIsInstance(config, list)

class TestGetInitialSeed(unittest.TestCase):
    def test_get_initial_seed_custom(self):
        initial_seed_name = "Custom"
        config = ["", "", "", "", "[[1, 0], [0, 1]]"]
        expected_seed = [[1, 0], [0, 1]]
        self.assertEqual(get_initial_seed(initial_seed_name, config), expected_seed)
    
    def test_get_initial_seed_known(self):
        initial_seed_name = "Glider"
        config = ["", "", "", "", "[[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0]]"]
        expected_seed = seeds["Glider"]
        self.assertEqual(get_initial_seed(initial_seed_name, config), expected_seed)


if __name__ == "__main__":
    unittest.main()

    