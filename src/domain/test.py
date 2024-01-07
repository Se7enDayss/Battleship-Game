import tkinter as tk
from tkinter import messagebox, font
from board import Board


class BattleshipGUI:
    def __init__(self, master):
        self.master = master
        master.title("Battleship Game")

        # Initialize the player and computer boards
        self.player_board = Board()
        self.computer_board = Board()

        # Create board frames
        self.player_board_frame = tk.Frame(master)
        self.computer_board_frame = tk.Frame(master)

        # Custom font for buttons and title
        button_font = font.Font(size=20)
        title_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Title Label
        self.title_label = tk.Label(master, text="Battleship Game", fg="blue", font=title_font)
        self.title_label.pack(pady=40)

        # Start Game Button
        self.start_button = tk.Button(master, text="Start Game", font=button_font, command=self.start_game)
        self.start_button.pack(pady=20, padx=20, ipadx=50, ipady=20)

        # View Rules Button
        self.rules_button = tk.Button(master, text="View Rules", font=button_font, command=self.view_rules)
        self.rules_button.pack(pady=20, padx=20, ipadx=50, ipady=20)

        # Exit Button
        self.exit_button = tk.Button(master, text="Exit", font=button_font, command=self.exit_game)
        self.exit_button.pack(pady=20, padx=20, ipadx=50, ipady=20)

    def start_game(self):
        # Hide menu buttons and initialize game board
        self.start_button.pack_forget()

        # Create and display the game boards
        self.create_board(self.player_board_frame, "Player Board", self.player_board, read_only=False)
        self.create_board(self.computer_board_frame, "Computer Board", self.computer_board, read_only=True)

        # Pack the frames with padding to create space between them
        self.player_board_frame.pack(side="left", fill="both", expand=True, padx=(20, 10))
        self.computer_board_frame.pack(side="right", fill="both", expand=True, padx=(10, 20))

    def create_board(self, parent_frame, title, board, read_only):
        # Title for the board
        tk.Label(parent_frame, text=title).grid(row=0, columnspan=11)

        # Create column labels (A-J)
        for col in range(10):
            tk.Label(parent_frame, text=chr(65 + col)).grid(row=1, column=col + 1)

        # Create row labels (1-10) and buttons for each cell
        self.buttons = {}
        for row in range(10):
            # Row label
            tk.Label(parent_frame, text=str(row + 1)).grid(row=row + 2, column=0)

            for col in range(10):
                cell_value = board.get_value(f'{row + 1}{chr(65 + col)}')
                button = tk.Button(parent_frame, text=cell_value, width=2)
                button.grid(row=row + 2, column=col + 1)
                self.buttons[(row, col)] = button

                # Bind a function to the button click (if needed for game logic)
                if not read_only:
                    button.config(command=lambda r=row, c=col: self.cell_clicked(r, c, board))

        # Store the board object for later use
        self.board = board
    def cell_clicked(self, row, col, board):
        # This function gets executed when a cell is clicked.
        # Implement game logic here.
        print(f"Cell clicked at Row: {row}, Col: {col}")
        # Here you can modify the board state and update the GUI accordingly
    def update_board(self):
        # Update the GUI to reflect the current state of the board
        for (row, col), button in self.buttons.items():
            cell_value = self.board.get_value(f'{row+1}{chr(65 + col)}')
            button.config(text=cell_value)
    def view_rules(self):
        rules = "Rules of the game..."
        messagebox.showinfo("Game Rules", rules)

    def exit_game(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    BattleshipGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
