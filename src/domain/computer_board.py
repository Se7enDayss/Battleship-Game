import random

from colorama import Fore

from src.domain.board import Board

class ComputerBoard(Board):

    def __init__(self):
        super().__init__()
        self.place_random_ships()
    def place_random_ships(self):
        """
        The function places random ships on the computer board
        :return:
        """
        ships = {'Carrier': 5, 'Battleship': 4, 'Destroyer': 3, 'Submarine': 3, 'Patrol Boat': 2}
        for ship_name, length in ships.items():
            placed = False
            while not placed:
                start_row = random.randint(0, 9)
                start_col = random.randint(0, 9)
                horizontal = random.choice([True, False])
                if self.can_place_ship(start_row, start_col, length, horizontal):
                    self.place_random_ship(start_row, start_col, length, horizontal, ship_name)
                    placed = True

    def can_place_ship(self, row, col, length, horizontal):
        """
        Check if the ship can be placed at a specific starting coord, considering the orientation
        :param row:
        :param col:
        :param length:
        :param horizontal:
        :return:
        """
        if horizontal:
            if col + length > 10:
                return False
            for i in range(col, col + length):
                if self.get_value(pack_coords(row, i)) != '~':
                    return False
        else:
            if row + length > 10:
                return False
            for i in range(row, row + length):
                if self.get_value(pack_coords(i, col)) != '~':
                    return False
        return True

    def place_random_ship(self, row, col, length, horizontal, ship_name):
        # Place the ship on the board
        for i in range(length):
            if horizontal:
                self.set_value(pack_coords(row, col + i), 'S')
            else:
                self.set_value(pack_coords(row + i, col), 'S')
        self.ships[ship_name] = {
            'start_coord': (row, col),
            'end_coord': (row, col + length - 1) if horizontal else (row + length - 1, col),
            'length': length,
            'hits': 0
        }


class ComputerHiddenEnemyBoard(Board):
    def __init__(self, enemy_board: Board):
        super().__init__()
        self.enemy_board = enemy_board
        self.target_mode = False
        self.last_hit = None
        self.first_hit = None
        self.hit_direction = None

    def hit(self):
        if self.target_mode:
            coords = self.calculate_target_hit()
        else:
            coords = self.random_hit()

        if self.enemy_board.get_value(coords) == 'S':
            self.handle_hit_on_target(coords)
        else:
            self.handle_miss(coords)

        return coords

    def handle_hit_on_target(self, coords):
        self.enemy_board.increment_hit_count(coords)
        self.set_value(coords, Fore.RED + 'X' + Fore.RESET)
        self.enemy_board.set_value(coords, Fore.RED + 'S' + Fore.RESET)
        self.enemy_board.total_hits += 1

        if not self.target_mode:
            self.first_hit = coords
            self.target_mode = True
        else:
            self.update_hit_direction(self.last_hit, coords)

        self.last_hit = coords

        if self.enemy_board.is_ship_sunk(coords):
            self.reset_target_mode()

    def handle_miss(self,coords):
        self.set_value(coords, 'X')
        if self.target_mode and self.hit_direction:
            if self.last_hit != self.first_hit:
                self.reverse_hit_direction()
            else:
                # If reverse hit direction misses without sinking a ship it means there are 2 adjacent ships
                self.last_hit = self.first_hit
                self.hit_direction = None

    def reset_target_mode(self):
        self.target_mode = False
        self.hit_direction = None
        self.last_hit = None
        self.first_hit = None

    def update_hit_direction(self, previous_hit, current_hit):
        prev_row, prev_col = self.convert_coordinates(previous_hit)
        curr_row, curr_col = self.convert_coordinates(current_hit)
        if prev_row == curr_row:
            self.hit_direction = 'horizontal'
        elif prev_col == curr_col:
            self.hit_direction = 'vertical'

    def reverse_hit_direction(self):
        self.last_hit = self.first_hit

    def calculate_target_hit(self):
        last_hit_row, last_hit_col = self.convert_coordinates(self.last_hit)

        # Define potential targets
        if self.hit_direction == 'horizontal':
            potential_targets = [(last_hit_row, last_hit_col - 1), (last_hit_row, last_hit_col + 1)]
        elif self.hit_direction == 'vertical':
            potential_targets = [(last_hit_row - 1, last_hit_col), (last_hit_row + 1, last_hit_col)]
        else:
            potential_targets = [
                (last_hit_row - 1, last_hit_col),
                (last_hit_row + 1, last_hit_col),
                (last_hit_row, last_hit_col - 1),
                (last_hit_row, last_hit_col + 1),
            ]

        valid_targets = [pack_coords(row, col) for row, col in potential_targets
                         if 0 <= row < 10 and 0 <= col < 10 and self.is_valid_hit(pack_coords(row, col))]

        if valid_targets:
            return random.choice(valid_targets)
        else:
            if self.last_hit != self.first_hit:
                self.reverse_hit_direction()
                return self.calculate_target_hit()
            else:
                return self.random_hit()

    def random_hit(self):
        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            coords = pack_coords(row, col)
            if self.is_valid_hit(coords):
                return coords

    def is_valid_hit(self, coords):
        return self.get_value(coords) == '~'

def pack_coords(row,col):
    coords=str(row+1)
    coords+=chr(col+ord('A'))
    return coords

# board=Board()
# hidden=ComputerHiddenEnemyBoard(board)
# hidden.hit()
# print(hidden)

