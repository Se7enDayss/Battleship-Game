import random

from colorama import Fore

from src.domain.board import Board

class ComputerBoard(Board):

    def __init__(self):
        super().__init__()
        #self.ships = {}
        self.place_random_ships()
    def place_random_ships(self):
        ships = {'Carrier': 5, 'Battleship': 4, 'Destroyer': 3, 'Submarine': 3, 'Patrol Boat': 2}
        for length in ships.values():
            placed = False
            while not placed:
                start_row = random.randint(0, 9)
                start_col = random.randint(0, 9)
                horizontal = random.choice([True, False])

                if self.can_place_ship(start_row, start_col, length, horizontal):
                    self.place_random_ship(start_row, start_col, length, horizontal)
                    placed = True
    def can_place_ship(self, row, col, length, horizontal):
        # Check if the ship can be placed at the given starting position
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

    def place_random_ship(self, row, col, length, horizontal):
        #start_coord = pack_coords(row, col)
        #self.ships[start_coord] = {'length': length, 'hits': 0}

        for i in range(length):
            if horizontal:
                self.set_value(pack_coords(row, col + i),'S')
            else:
                self.set_value(pack_coords(row + i, col),'S')

class ComputerHiddenEnemyBoard(Board):
    def __init__(self,enemy_board:Board):
        super().__init__()
        self.enemy_board=enemy_board

    def hit(self):
        while True:
            rand_row=str(random.randint(1,10))
            rand_col=chr(random.randint(ord('A'),ord('J')))
            coords = rand_row+rand_col

            if self.is_valid_hit(coords):
                if self.enemy_board.get_value(coords) == 'S':
                    self.set_value(coords, Fore.RED + 'X' + Fore.RESET)
                    self.enemy_board.set_value(coords,Fore.RED+'S'+Fore.RESET)
                    self.enemy_board.total_hits += 1
                else:
                    self.set_value(coords, 'X')
                return coords

    def is_valid_hit(self,coords):
        return self.get_value(coords)=='~'


def pack_coords(row,col):
    coords=str(row+1)
    coords+=chr(col+ord('A'))
    return coords

#board=Board()
#hidden=ComputerHiddenEnemyBoard(board)
#hidden.hit()
#print(hidden)

