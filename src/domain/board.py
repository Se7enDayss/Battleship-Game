import random
from colorama import Fore


class Board:
    def __init__(self):
        self.__data = [['~' for _ in range(10)] for _ in range(10)]
        self.total_hits = 0

    def __str__(self):
        board_representation ='   ' + ' '.join([chr(i) for i in range(ord('A'), ord('K'))]) + '\n'

        for i in range(len(self.__data)):
            row_num = str(i + 1).ljust(2)  # Left-align the row number in a 2-character field
            board_representation += row_num + ' ' + ' '.join(self.__data[i]) + '\n'

        return board_representation

    def convert_coordinates(self, user_coords: str):
        """
        Convert user-friendly coordinates (e.g., '1A', '10J', etc.) to numerical indices.
        """
        if len(user_coords) < 2 or len(user_coords) > 3:
            raise ValueError("Invalid coordinates length. Use format like '1A', '10J', etc.\n")

        if user_coords[:-1].isdigit() and user_coords[-1].isalpha():
            row = int(user_coords[:-1]) - 1
            column = ord(user_coords[-1].upper()) - ord('A')
        else:
            raise ValueError("Invalid coordinates format. Use format like '1A', '10J', etc.\n")

        if row < 0 or row >= 10 or column < 0 or column >= 10:
            raise ValueError("Coordinates are out of the board's range.\n")

        return row, column

    def set_value(self, user_coords: str, new_value):
        """
        Set the value of the cell at the given user-friendly coordinates.
        """
        row, column = self.convert_coordinates(user_coords)
        self.__data[row][column] = new_value

    def get_value(self, user_coords: str):
        """
        Get the value of the cell at the given user-friendly coordinates.
        """
        row, column = self.convert_coordinates(user_coords)
        return self.__data[row][column]

    def is_valid_placement(self, row1, col1, row2, col2):
        """
        Check if the ship placement is valid (no overlap and within bounds) assuming row1 , col1 < row2, col2
        """
        if row1 == row2:
            for col in range(col1, col2 + 1):
                if self.__data[row1][col] != '~':
                    return False
        elif col1 == col2:
            for row in range(row1, row2 + 1):
                if self.__data[row][col1] != '~':
                    return False
        return True

    def place_ship(self, coords1: str, coords2: str):
        row1, col1 = self.convert_coordinates(coords1)
        row2, col2 = self.convert_coordinates(coords2)

        # Swap coordinates if necessary to simplify logic
        if row1 == row2 and col1 > col2 or col1 == col2 and row1 > row2:
            row1, col1, row2, col2 = row2, col2, row1, col1

        # Check for valid placement
        if not self.is_valid_placement(row1, col1, row2, col2):
            raise ValueError("Invalid placement! The ship overlaps with another ship or is out of bounds.\n")

        if row1 == row2:
            for i in range(col1, col2 + 1):
                self.__data[row1][i] = 'S'
        elif col1 == col2:
            for i in range(row1, row2 + 1):
                self.__data[i][col1] = 'S'
        else:
            raise ValueError("Invalid Coordinates! You can only place a ship horizontally or vertically.\n")

    def get_lenght_between_coords(self,coords1,coords2):
        """
        Get's the lenght in cells between 2 inputs
        :param coords1:
        :param coords2:
        :return:
        """
        row1,col1=self.convert_coordinates(coords1)
        row2,col2=self.convert_coordinates(coords2)

        # Swap coordinates if necessary to simplify logic
        if row1 == row2 and col1 > col2 or col1 == col2 and row1 > row2:
            row1, col1, row2, col2 = row2, col2, row1, col1

        if row1==row2:
            return col2-col1+1
        elif col1==col2:
            return row2-row1+1
        else:
            raise ValueError("Invalid Coordinates! You can only place a ship horizontally or vertically.")
    def is_game_over(self):
        return self.total_hits == 17

class HiddenEnemyBoard(Board):
    def __init__(self,enemy_board:Board):
        super().__init__()
        self.enemy_board=enemy_board
    def hit(self,coords):
        if not self.is_valid_hit(coords):
            raise ValueError("You already hit this cell! Take another guess!")
        if self.enemy_board.get_value(coords)== 'S':
            self.set_value(coords,Fore.RED + 'X' + Fore.RESET)
            self.enemy_board.total_hits += 1
            return True
        else:
            self.set_value(coords,'X')
            return False
    def is_valid_hit(self,coords):
        return self.get_value(coords)=='~'


