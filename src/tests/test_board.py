import unittest
from unittest import TestCase
from colorama import Fore
from src.domain.board import Board, HiddenEnemyBoard

class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        str_board = str(self.board)
        self.assertTrue(all(row.count('~') == 10 for row in str_board.split('\n')[1:11]))
        self.assertEqual(self.board.total_hits, 0)

    def test_str(self):
        str_board = str(self.board)
        self.assertIn(' A B C D E F G H I J', str_board)

    def test_convert_coordinates(self):
        self.assertEqual(self.board.convert_coordinates('1A'), (0, 0))
        self.assertEqual(self.board.convert_coordinates('10J'), (9, 9))
        with self.assertRaises(ValueError):
            self.board.convert_coordinates('11A')
        with self.assertRaises(ValueError):
            self.board.convert_coordinates('A1')

    def test_set_and_get_value(self):
        self.board.set_value('1A', 'X')
        self.assertEqual(self.board.get_value('1A'), 'X')

    def test_is_valid_placement(self):
        self.assertTrue(self.board.is_valid_placement(0, 0, 0, 4))
        self.assertFalse(self.board.is_valid_placement(0, 0, 0, 10))

    def test_place_ship(self):
        self.board.place_ship('1A', '1D', 'Destroyer')
        self.assertEqual(self.board.get_value('1A'), 'S')
        self.assertEqual(self.board.get_value('1D'), 'S')
        self.assertIn('Destroyer', self.board.ships)

    def test_get_length_between_coords(self):
        self.assertEqual(self.board.get_length_between_coords('1A', '1D'), 4)
        self.assertEqual(self.board.get_length_between_coords('1A', '4A'), 4)

    def test_increment_hit_count(self):
        self.board.place_ship('1A', '1D', 'Destroyer')
        self.board.increment_hit_count('1A')
        self.assertEqual(self.board.ships['Destroyer']['hits'], 1)

    def test_check_if_ship_sunk(self):
        self.board.place_ship('1A', '1D', 'Destroyer')
        for coord in ['1A', '1B', '1C', '1D']:
            self.board.increment_hit_count(coord)
        self.assertEqual(self.board.check_if_ship_sunk('1D'), 'Destroyer')

    def test_is_ship_sunk(self):
        self.board.place_ship('1A', '1D', 'Destroyer')
        for coord in ['1A', '1B', '1C', '1D']:
            self.board.increment_hit_count(coord)
        self.assertTrue(self.board.is_ship_sunk('1D'))

    def test_is_within_ship(self):
        self.board.place_ship('1A', '1D', 'Destroyer')
        self.assertTrue(self.board.is_within_ship(0, 0, self.board.ships['Destroyer']))

    def test_is_game_over(self):
        self.assertFalse(self.board.is_game_over())


class TestHiddenEnemyBoard(unittest.TestCase):
    def setUp(self):
        self.player_board = Board()
        self.hidden_enemy_board = HiddenEnemyBoard(self.player_board)

    def test_hit(self):
        self.player_board.set_value('1A', 'S')
        hit_result = self.hidden_enemy_board.hit('1A')
        self.assertTrue(hit_result)
        self.assertEqual(self.hidden_enemy_board.get_value('1A'), Fore.RED + 'X' + Fore.RESET)



