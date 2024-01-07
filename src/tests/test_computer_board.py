from unittest.mock import patch
from unittest import TestCase

from colorama import Fore

from src.domain.computer_board import ComputerBoard,ComputerHiddenEnemyBoard
from src.domain.board import Board

class TestComputerBoard(TestCase):
    def setUp(self):
        self.board = ComputerBoard()

    def test_ship_placement_within_bounds(self):
        for ship in self.board.ships.values():
            start_row, start_col = ship['start_coord']
            end_row, end_col = ship['end_coord']
            self.assertTrue(0 <= start_row < 10)
            self.assertTrue(0 <= start_col < 10)
            self.assertTrue(0 <= end_row < 10)
            self.assertTrue(0 <= end_col < 10)

    def test_ships_do_not_overlap(self):
        occupied = set()
        for ship in self.board.ships.values():
            start_row, start_col = ship['start_coord']
            end_row, end_col = ship['end_coord']
            horizontal = start_row == end_row
            for i in range(ship['length']):
                coord = (start_row, start_col + i) if horizontal else (start_row + i, start_col)
                self.assertNotIn(coord, occupied)
                occupied.add(coord)
