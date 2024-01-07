from colorama import Fore


class Manage_Ships_UI:
    @staticmethod
    def place_carrier(board):
        while True:
            try:
                carrier_sc = input("Enter CARRIER's starting coords (5 cells in total): ")
                carrier_ec = input("Enter CARRIER's ending coords: ")
                board.place_ship(carrier_sc,carrier_ec,"Carrier")
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
                board.place_ship(battleship_sc, battleship_ec,"Battleship")
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
                board.place_ship(destroyer_sc, destroyer_ec,"Destroyer")
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
                board.place_ship(submarine_sc, submarine_ec,"Submarine")
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
                board.place_ship(patrolboat_sc, patrolboat_ec,"Patrol Boat")
                print(Fore.CYAN + "successfully placed the patrol boat\n" + Fore.RESET)
                print(board)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)