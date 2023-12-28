from colorama import Fore


class Manage_Ships_UI:
    @staticmethod
    def place_carrier(board):
        while True:
            try:
                carrier_sc = input("Enter CARRIER's starting coords (5 cells in total): ")
                carrier_ec = input("Enter CARRIER's ending coords: ")
                lenght=board.get_lenght_between_coords(carrier_sc,carrier_ec)
                if lenght !=5:
                    raise ValueError(f"Invalid ship size({lenght})! CARRIER must occupy 5 cells!\n")
                board.place_ship(carrier_sc,carrier_ec)
                print(Fore.CYAN+ "successfully placed the carrier\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print (Fore.RED + str(e) + Fore.RESET)

    @staticmethod
    def place_battleship(board):
        while True:
            try:
                battleship_sc = input("Enter BATTLESHIP's starting coords (4 cells in total): ")
                battleship_ec = input("Enter BATTLESHIP's ending coords: ")
                lenght = board.get_lenght_between_coords(battleship_sc, battleship_ec)
                if lenght != 4:
                    raise ValueError(f"Invalid ship size({lenght})! BATTLESHIP must occupy 4 cells!\n")
                board.place_ship(battleship_sc, battleship_ec)
                print(Fore.CYAN + "successfully placed the battleship\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)

    @staticmethod
    def place_destroyer(board):
        while True:
            try:
                destroyer_sc = input("Enter DESTROYER's starting coords (3 cells in total): ")
                destroyer_ec = input("Enter DESTROYER's ending coords: ")
                lenght = board.get_lenght_between_coords(destroyer_sc, destroyer_ec)
                if lenght != 3:
                    raise ValueError(f"Invalid ship size({lenght})! DESTROYER must occupy 3 cells!\n")
                board.place_ship(destroyer_sc, destroyer_ec)
                print(Fore.CYAN + "successfully placed the destroyer\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)

    @staticmethod
    def place_submarine(board):
        while True:
            try:
                submarine_sc = input("Enter SUBMARINE's starting coords (3 cells in total): ")
                submarine_ec = input("Enter SUBMARINE's ending coords: ")
                lenght = board.get_lenght_between_coords(submarine_sc, submarine_ec)
                if lenght != 3:
                    raise ValueError(f"Invalid ship size({lenght})! SUBMARINE must occupy 3 cells!\n")
                board.place_ship(submarine_sc, submarine_ec)
                print(Fore.CYAN + "successfully placed the submarine\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)

    @staticmethod
    def place_patrol_boat(board):
        while True:
            try:
                patrolboat_sc = input("Enter PATROL BOAT's starting coords (2 cells in total): ")
                patrolboat_ec = input("Enter PATROL BOAT's ending coords: ")
                lenght = board.get_lenght_between_coords(patrolboat_sc, patrolboat_ec)
                if lenght != 2:
                    raise ValueError(f"Invalid ship size({lenght})! PATROL BOAT must occupy 2 cells!\n")
                board.place_ship(patrolboat_sc, patrolboat_ec)
                print(Fore.CYAN + "successfully placed the patrol boat\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)