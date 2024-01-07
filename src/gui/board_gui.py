import re
import tkinter as tk
import tkinter.font as font
class BoardGUI:
    def __init__(self, parent, title, board):
        self.board = board
        self.buttons = {}
        self.frame=tk.Frame(parent)
        self.create_board(parent, title)

    def enable_cell_clicks(self, on_click_callback):
            for (row, col), button in self.buttons.items():
                button.config(command=lambda r=row, c=col: on_click_callback(r, c))

    def disable_cell_clicks(self):
        for button in self.buttons.values():
            button.config(command=lambda: None)  # Bind to a no-op lambda function

    def create_board(self, parent, title):
        self.frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        tk.Label(self.frame, text=title,font=('Rockwell extra bold',16),fg='orange').grid(row=0, columnspan=11)

        for col in range(10):
            tk.Label(self.frame, text=chr(65 + col)).grid(row=1, column=col + 1)

        for row in range(10):
            tk.Label(self.frame, text=str(row + 1)).grid(row=row + 2, column=0)

            for col in range(10):
                cell_value = self.board.get_value(f'{row + 1}{chr(65 + col)}')
                button = tk.Button(self.frame, text=cell_value, width=2)
                button.grid(row=row + 2, column=col + 1)
                self.buttons[(row, col)] = button
                button.config(command=lambda r=row, c=col: self.cell_clicked(r, c))

    def cell_clicked(self, row, col):
        pass

    def hide_board(self):
        self.frame.pack_forget()

    def update_board(self):
        for (row, col), button in self.buttons.items():
            cell_value = self.board.get_value(f'{row + 1}{chr(65 + col)}')
            clean_value = remove_ansi_color_codes(cell_value)
            text_color='black'
            if cell_value != clean_value:
                button.config(text="",bg='red')
            else:
                button.config(text=clean_value,fg=text_color)

    def update_board_with_players_ships(self):
        for (row,col), button in self.buttons.items():
            cell_value = self.board.get_value(f'{row + 1}{chr(65 + col)}')
            clean_value = remove_ansi_color_codes(cell_value)
            if cell_value == 'S':
                button.config(text="",bg='grey')
            elif clean_value == 'S' and clean_value != cell_value:
                button.config(text="", bg='red')
            else:
                button.config(text=cell_value)

def remove_ansi_color_codes(text):
    # ANSI color code regex
    ansi_escape = re.compile(r'''
        \x1B  # ESC
        [@-_] # 7-bit C1 Fe
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]  # Final byte
    ''', re.VERBOSE)
    return ansi_escape.sub('', text)