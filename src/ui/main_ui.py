import re
from colorama import Fore
from src.domain.board import Board, HiddenEnemyBoard
from src.domain.computer_board import ComputerBoard,ComputerHiddenEnemyBoard
from src.ui.manage_ships_ui import Manage_Ships_UI

class MainUI:
    def __init__(self,printf,service):
        self.printf=printf
        self.service=service

    @staticmethod
    def length_without_ansi(string):
        # Regular expression to match ANSI escape codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return len(ansi_escape.sub('', string))

    def print_boards_side_by_side(self, board, hidden_board):
        board_lines = str(board).split('\n')
        hidden_lines = str(hidden_board).split('\n')

        # Find the maximum length of a line excluding ANSI codes
        max_length = max(self.length_without_ansi(line) for line in board_lines)

        print("\nYour board:".ljust(max_length + 4) + "Enemy board:")

        for line1, line2 in zip(board_lines, hidden_lines):
            # Adjust the left-justify amount to account for ANSI codes
            adjusted_length = max_length + 4 + (len(line1) - self.length_without_ansi(line1))
            formatted_line1 = line1.ljust(adjusted_length)
            print(formatted_line1 + line2)

    def ui_ai_try_hit(self, computer_hidden_board, board):
        print(Fore.CYAN + "\nIt's computer's turn to choose coordinates" + Fore.RESET)
        coords = computer_hidden_board.hit()
        print(f"The computer chose coordinates: {coords}")

        if board.get_value(coords) == Fore.RED + 'S' + Fore.RESET:
            print(Fore.RED + "Computer hit one of your ships!" + Fore.RESET)

            sunk_ship = board.check_if_ship_sunk(coords)
            if sunk_ship:
                print(Fore.YELLOW + f"Computer has sunk your {sunk_ship}!" + Fore.RESET)
        else:
            print(Fore.GREEN + "Computer missed!" + Fore.RESET)

    def ui_try_hit(self, hidden_board, enemy_board):
        print(Fore.CYAN + "It's your turn to choose coordinates" + Fore.RESET)
        while True:
            coords = input("Choose coordinates to hit: ")
            try:
                hit_result = hidden_board.hit(coords)
                if hit_result:
                    print(Fore.GREEN + "You hit a target!" + Fore.RESET)
                    sunk_ship = enemy_board.check_if_ship_sunk(coords)
                    if sunk_ship:
                        print(Fore.YELLOW + f"You have sunk the {sunk_ship}!" + Fore.RESET)
                else:
                    print(Fore.RED + "You missed!" + Fore.RESET)
                break
            except ValueError as e:
                print(Fore.RED + str(e) + Fore.RESET)

    def check_game_over(self, player_board, computer_board):
        """
        Check if the game is over and print the appropriate message.
        Returns True if the game is over, otherwise False.
        """
        if player_board.is_game_over():
            self.printf.lost()
            return True
        if computer_board.is_game_over():
            self.printf.won()
            return True
        return False
    def run(self):
        board=Board()
        computer_board=ComputerBoard()
        hidden_board=HiddenEnemyBoard(computer_board)
        computer_hidden_board=ComputerHiddenEnemyBoard(board)
        self.printf.welcome()
        while True:
            self.printf.options()
            v = input("Choose an option : ")
            if v == '1':
                self.service.clear_console()
                self.printf.ship_requirements()
                print (board)
                Manage_Ships_UI.place_carrier(board)
                Manage_Ships_UI.place_battleship(board)
                Manage_Ships_UI.place_destroyer(board)
                Manage_Ships_UI.place_submarine(board)
                Manage_Ships_UI.place_patrol_boat(board)
                self.service.clear_console()
                print(Fore.CYAN + "STARTING GAME..." + Fore.RESET)
                while True:
                    self.print_boards_side_by_side(board,hidden_board)
                    #print (computer_board) # DEBUGGING PURPOSES
                    #print(computer_hidden_board) # DEBUGGING PURPOSES
                    self.ui_try_hit(hidden_board,computer_board)
                    if self.check_game_over(board, computer_board):
                        break
                    self.ui_ai_try_hit(computer_hidden_board,board)
                    if self.check_game_over(board, computer_board):
                        break
                return
            elif v == '2':
                self.service.clear_console()
                self.printf.rules()
            elif v == '3':
                print (Fore.CYAN + "Exited the game! Thank you for playing!"+Fore.RESET)
                return
            else:
                print (Fore.RED + "Invalid option! Please choose a valid option!"+Fore.RESET)
