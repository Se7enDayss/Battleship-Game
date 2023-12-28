import re
from colorama import Fore
from src.domain.board import Board, HiddenEnemyBoard
from src.domain.computer_board import ComputerBoard,ComputerHiddenEnemyBoard
from src.ui.manage_ships_ui import Manage_Ships_UI
from src.ui.prints import PrintMessages
from src.services.main_service import MainService

class MainUI:
    def __init__(self,printf,service):
        self.printf=printf
        self.service=service

    #def print_boards(self,board,hidden_board):
    #    print("\nYour board: ")
    #    print(board)
    #    print("Enemy board: ")
    #   print(hidden_board)

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

    def ui_ai_try_hit(self,computer_hidden_board,board):
        coords=computer_hidden_board.hit()
        print(Fore.CYAN + "\nIt's computer's turn to guess coordinates" + Fore.RESET)
        print(f"The computer guessed coordinates: {coords}")
        if board.get_value(coords) == Fore.RED + 'S' + Fore.RESET:
            print(Fore.RED+"Computer hit one of your ships!"+Fore.RESET)
        else:
            print(Fore.GREEN+"Computer missed!"+Fore.RESET)

    def ui_try_hit(self,hidden_board):
        print(Fore.CYAN + "It's your turn to guess coordinates"+Fore.RESET)
        coords = input("Guess coordinates to hit: ")
        try:
            if hidden_board.hit(coords):
                print(Fore.GREEN + "You hit a target!" + Fore.RESET)
            else:
                print(Fore.RED + "You missed!" + Fore.RESET)
        except ValueError as e :
            print(Fore.RED + str(e) + Fore.RESET)
    def run(self):
        board=Board()
        computer_board=ComputerBoard()
        hidden_board=HiddenEnemyBoard(computer_board)
        computer_hidden_board=ComputerHiddenEnemyBoard(board)
        self.printf.welcome()
        input("Press enter to play...\n")
        self.service.clear_console()
        self.printf.rules()
        self.printf.ship_requirements()
        print (board)
        Manage_Ships_UI.place_carrier(board)
        Manage_Ships_UI.place_battleship(board)
        Manage_Ships_UI.place_destroyer(board)
        Manage_Ships_UI.place_submarine(board)
        Manage_Ships_UI.place_patrol_boat(board)
        print("Starting game...\n")
        while True:
            self.print_boards_side_by_side(board,hidden_board)
            print(computer_board) # Testing Purposes
            if board.is_game_over():
                print("You lost! :)")
                break
            if computer_board.is_game_over():
                print("You won! :)")
                break
            self.ui_try_hit(hidden_board)
            self.ui_ai_try_hit(computer_hidden_board,board)

#START#
printf=PrintMessages()
service=MainService()
ui=MainUI(printf,service)
ui.run()