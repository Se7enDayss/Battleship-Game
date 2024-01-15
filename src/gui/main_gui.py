import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import pygame

from colorama import Fore

from src.domain.board import Board, HiddenEnemyBoard
from src.domain.computer_board import ComputerBoard, ComputerHiddenEnemyBoard
from src.gui.board_gui import BoardGUI

class BattleshipGUI:
    def __init__(self, master):
        self.master = master
        master.title("Battleship Game")
        master.geometry('600x450')


        # Load and play background music
        pygame.mixer.init()
        self.sound_on = True

        # Sound on/off button
        self.sound_button = tk.Button(master, text="Sound On", command=self.toggle_sound,font=('Rockwell extra bold',12))
        self.sound_button.place(relx=0.98, rely=0.98, anchor='se')

        self.background_music=pygame.mixer.Sound(r'D:\Python Projects\GitHub\a10-Se7enDayss\music.mp3')
        self.background_music.play(-1)
        self.hit_music=pygame.mixer.Sound(r'D:\Python Projects\GitHub\a10-Se7enDayss\explosion.mp3')
        self.splash_music=pygame.mixer.Sound(r'D:\Python Projects\GitHub\a10-Se7enDayss\splash.mp3')
        self.background_music.set_volume(0.1)
        self.splash_music.set_volume(0.2)
        self.hit_music.set_volume(1)


        self.player_board_gui = None
        self.player_hidden_board_gui = None
        self.ship_placement_frame = None
        self.is_player_turn = True
        self.current_ship_index = 0
        self.ships = ["Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat"]

        # Remove the maximize button and prevent resizing the window
        master.resizable(False, False)

        master.attributes('-fullscreen', False)

        # Load the background image
        image = Image.open(r'D:\Python Projects\GitHub\a10-Se7enDayss\background3.png')
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Initialize the boards
        self.player_board = Board()
        self.computer_board = ComputerBoard()
        self.player_hidden_board = HiddenEnemyBoard(self.computer_board)
        self.computer_hidden_board = ComputerHiddenEnemyBoard(self.player_board)

        # Custom font for buttons and title
        button_font = font.Font(size=14,family="Rockwell extra bold")
        title_font = font.Font(family="Rockwell extra bold", size=36)

        # Computer Guess Label
        self.computer_guess_label = tk.Label(master, text="")
        self.computer_result_label = tk.Label(master, text="")
        self.computer_sunk_label = tk.Label(master,text="")

        # Player Guess Label
        self.player_guess_label = tk.Label(master, text="")
        self.player_result_label = tk.Label(master, text="")
        self.player_sunk_label = tk.Label(master,text="")

        # Title Label
        self.title_label = tk.Label(master, text="BATTLESHIP GAME", font=title_font)
        self.title_label.pack(pady=30,padx=30)

        # Start Game Button
        self.start_button = tk.Button(master, text="START GAME", font=('Rockwell extra bold', 20), command=self.start_game,bg='green',fg='white')
        self.start_button.pack(pady=20, padx=20, ipadx=30, ipady=10)

        # View Rules Button
        self.rules_button = tk.Button(master, text="VIEW RULES", font=button_font, command=self.view_rules,bg='blue',fg='white')
        self.rules_button.pack(pady=10, padx=20, ipadx=30, ipady=10)

        # Exit Button
        self.exit_button = tk.Button(master, text="EXIT", bg='red',font=button_font, command=self.exit_game)
        self.exit_button.pack(pady=10, padx=20, ipadx=30, ipady=10)

    def toggle_sound(self):
        if self.sound_on:
            pygame.mixer.pause()
            self.sound_button.config(text="Sound Off")
            self.sound_on = False
        else:
            pygame.mixer.unpause()
            self.sound_button.config(text="Sound On")
            self.sound_on = True

    def start_game(self):
        self.master.geometry('')
        self.background_label.place_forget()
        self.start_button.pack_forget()
        self.player_board_gui = BoardGUI(self.master, "Player Board", self.player_board)
        self.player_board_gui.enable_cell_clicks(self.cell_clicked)
        self.create_ship_placement_form()
        #self.start_gameplay()

    def start_gameplay(self):
        self.player_hidden_board_gui = BoardGUI(self.master, "Enemy Board", self.player_hidden_board)

        self.user_turn_label = tk.Label(self.master, text="Your turn:\n Click on the enemy board to hit a cell", fg="blue", font=('Rockwell extra bold', 20),width=40)
        self.computer_turn_label = tk.Label(self.master, text="Computer's turn...", fg="blue", font=('Rockwell extra bold', 20),width=40)

        self.process_turn()

        # Checking the 'you won' message
        #self.computer_board.total_hits = 17

    def you_won_message(self):
        self.start_button.pack_forget()
        self.rules_button.pack_forget()
        self.user_turn_label.pack_forget()
        self.player_guess_label.pack_forget()
        self.player_result_label.pack_forget()
        self.computer_turn_label.pack_forget()
        self.computer_guess_label.pack_forget()
        self.computer_result_label.pack_forget()
        self.computer_sunk_label.pack_forget()
        self.player_sunk_label.pack_forget()
        game_over_label = tk.Label(self.master, text="Congratulations!\n You won! :)", font=('Rockwell extra bold', 36), fg='green')
        game_over_label.pack(side='top',expand=True,pady=20, padx=20)
    def you_lost_message(self):
        self.start_button.pack_forget()
        self.rules_button.pack_forget()
        self.user_turn_label.pack_forget()
        self.player_guess_label.pack_forget()
        self.player_result_label.pack_forget()
        self.computer_turn_label.pack_forget()
        self.computer_guess_label.pack_forget()
        self.computer_result_label.pack_forget()
        self.computer_sunk_label.pack_forget()
        self.player_sunk_label.pack_forget()
        game_over_label = tk.Label(self.master, text="You lost! :(", font=('Rockwell extra bold', 36), fg='red')
        game_over_label.pack(side='top', expand=True, pady=20, padx=20)
    def process_turn(self):
        if self.player_board.is_game_over():
            self.you_lost_message()
            return
        if self.computer_board.is_game_over():
            self.you_won_message()
            return
        if self.is_player_turn:
            self.computer_turn_label.pack_forget()
            self.computer_guess_label.pack_forget()
            self.computer_result_label.pack_forget()
            self.computer_sunk_label.pack_forget()
            self.user_turn_label.pack(pady=(50,10))
            self.player_hidden_board_gui.enable_cell_clicks(self.enemy_cell_clicked)
        else:
            self.user_turn_label.pack_forget()
            self.player_guess_label.pack_forget()
            self.player_result_label.pack_forget()
            self.player_sunk_label.pack_forget()
            self.computer_turn_label.pack(pady=(50,10))
            self.master.after(1000,self.computer_try_hit)


    def enemy_cell_clicked(self, row, col):
        self.player_hidden_board_gui.disable_cell_clicks()
        coord = f"{row + 1}{chr(col + ord('A'))}"
        try:
            hit_result = self.player_hidden_board.hit(coord)
            self.player_guess_label.config(text=f"You chose: {row + 1}{chr(col + ord('A'))}",font=('Rockwell extra bold',14))
            self.player_guess_label.pack(pady=(0,10))
            if hit_result:
                if self.sound_on:
                    self.hit_music.play()

                self.player_result_label.config(text="You hit one of the ships!",fg='green',font=('Rockwell extra bold',22))
                self.player_result_label.pack(pady=20)
                sunk_ship = self.computer_board.check_if_ship_sunk(f"{row + 1}{chr(col + ord('A'))}")
                if sunk_ship:
                    self.player_sunk_label.config(text=f"You sunk the {sunk_ship}!", fg="orange",font=('Rockwell extra bold',16))
                    self.player_sunk_label.pack(pady=10)

            else:
                if self.sound_on:
                    self.splash_music.play()
                self.player_result_label.config(text="You missed!", fg="red",font=('Rockwell extra bold',22))
                self.player_result_label.pack(pady=20)

            self.player_hidden_board_gui.update_board()

            self.is_player_turn = False
            self.master.after(1000, self.process_turn)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.player_hidden_board_gui.enable_cell_clicks(self.enemy_cell_clicked)



    def computer_try_hit(self):
        coords = self.computer_hidden_board.hit()
        self.computer_guess_label.config(text=f"Computer chose: {coords}",font=('Rockwell extra bold',14))
        self.computer_guess_label.pack(pady=(0,10))

        if self.player_board.get_value(coords) == Fore.RED + 'S' + Fore.RESET:
            if self.sound_on:
                self.hit_music.play()

            self.computer_result_label.config(text="Computer hit one of your ships!", fg="red",font=('Rockwell extra bold',22))
            self.computer_result_label.pack(pady=20)
            self.player_board_gui.update_board_with_players_ships()

            sunk_ship = self.player_board.check_if_ship_sunk(coords)
            if sunk_ship:
                self.computer_sunk_label.config(text=f"Computer has sunk your {sunk_ship}!", fg="orange",font=('Rockwell extra bold',16))
                self.computer_sunk_label.pack(pady=10)
        else:
            if self.sound_on:
                self.splash_music.play()

            self.player_board.set_value(coords,'X')
            self.player_board_gui.update_board_with_players_ships()
            self.computer_result_label.config(text="Computer missed!", fg="green",font=('Rockwell extra bold',22))
            self.computer_result_label.pack(pady=20)

        self.is_player_turn = True
        self.master.after(1000, self.process_turn)

    def update_ship_placement_info(self, info):
        if hasattr(self, 'ship_placement_info_label'):
            self.ship_placement_info_label.config(text=info)
        else:
            self.ship_placement_info_label = tk.Label(self.ship_placement_frame, text=info)
            self.ship_placement_info_label.pack(pady=10)

    def place_ship_with_selected_coords(self):
        start_coord = f'{self.selected_start_coord[0] + 1}{chr(65 + self.selected_start_coord[1])}'
        end_coord = f'{self.selected_end_coord[0] + 1}{chr(65 + self.selected_end_coord[1])}'
        current_ship = self.ships[self.current_ship_index]

        try:
            self.player_board.place_ship(start_coord, end_coord, current_ship)
            self.player_board_gui.update_board_with_players_ships()

            messagebox.showinfo("Ship Placed", f"{current_ship} successfully placed from {start_coord} to {end_coord}")

            self.clear_ship_placement_form()

            self.current_ship_index += 1
            if self.current_ship_index < len(self.ships):
                self.create_ship_placement_form()
            else:
                messagebox.showinfo("All Ships Placed", "Game is starting...")
                self.player_board_gui.disable_cell_clicks()
                self.ship_placement_frame.pack_forget()
                self.ship_placement_frame = None

                # STARTING THE GAME
                self.start_gameplay()

        except ValueError as e:
            messagebox.showerror("Invalid Placement", str(e))
            self.clear_ship_placement_form()
            self.create_ship_placement_form()

    def clear_ship_placement_form(self):
        if hasattr(self, 'selected_start_coord'):
            delattr(self, 'selected_start_coord')
        if hasattr(self, 'selected_end_coord'):
            delattr(self, 'selected_end_coord')
        if self.ship_placement_frame:
            self.ship_placement_frame.destroy()
            self.ship_placement_frame = tk.Frame(self.master)
            self.ship_placement_frame.pack()

    def create_ship_placement_form(self):
        if self.current_ship_index >= len(self.ships):
            self.ship_placement_frame.pack_forget()
            return

        ship = self.ships[self.current_ship_index]
        ship_length = {"Carrier": 5, "Battleship": 4, "Destroyer": 3, "Submarine": 3, "Patrol Boat": 2}

        if self.ship_placement_frame:
            self.ship_placement_frame.destroy()
        self.ship_placement_frame = tk.Frame(self.master)
        self.ship_placement_frame.pack()

        ship_info = (f"Place your {ship} (Length: {ship_length[ship]} cells)\n"
                     "Select ship's START and END cells")
        tk.Label(self.ship_placement_frame, text=ship_info, fg='green',font=('Rockwell extra bold', 16), justify='center').pack(
            pady=(100,10),padx=20)

        self.ship_placement_info_label = tk.Label(self.ship_placement_frame, text="",font=('Rockwell extra bold',14))
        self.ship_placement_info_label.pack(pady=10)

        place_ship_button = tk.Button(self.ship_placement_frame, text=f"Place {ship}",width=14,height=2,font=('Rockwell extra bold',14),fg='green',command=self.place_ship_with_selected_coords)
        place_ship_button.pack(pady=10)

    def cell_clicked(self, row, col):
        if hasattr(self, 'selected_end_coord'):
            delattr(self, 'selected_start_coord')
            delattr(self, 'selected_end_coord')
            selected_coords_info = "Select start coordinate"
        elif hasattr(self, 'selected_start_coord'):
            self.selected_end_coord = (row, col)
            selected_coords_info = f"Selected Coordinates: Start: {self.selected_start_coord[0] + 1}{chr(65 + self.selected_start_coord[1])}, End: {row + 1}{chr(65 + col)}"
        else:
            self.selected_start_coord = (row, col)
            selected_coords_info = f"Start coordinate selected at {row + 1}{chr(65 + col)}"

        self.update_ship_placement_info(selected_coords_info)
    def view_rules(self):
        rules = """
The game is played on four grids, two for each player. The grids are typically square – usually 
10×10 – and the individual squares in the grid are identified by letter and number. On one grid the 
player arranges ships and records the shots by the opponent. On the other grid, the player records their own 
shots.

Before play begins, each player secretly arranges their ships on their primary grid. Each ship occupies a number of 
consecutive squares on the grid, arranged either horizontally or vertically. The number of squares for each ship is 
determined by the type of ship. The ships cannot overlap (i.e., only one ship can occupy any given square in the 
grid). The types and numbers of ships allowed are the same for each player. These may vary depending on the rules. 
The ships should be hidden from players sight and it's not allowed to see each other's pieces. The game is a 
discovery game which players need to discover their opponents ship positions. )
        
After the ships have been positioned, the game proceeds in a series of rounds. In each round, each player 
takes a turn to announce a target square in the opponent's grid which is to be shot at. The opponent 
announces whether or not the square is occupied by a ship. If it is a "hit", the player who is hit marks this 
on their own or "ocean" grid (with a red peg in the pegboard version), and announces what ship was hit. The 
attacking player marks the hit or miss on their own "tracking" or "target" grid with a pencil marking in the 
paper version of the game, or the appropriate color peg in the pegboard version (red for "hit", 
white for "miss"), in order to build up a picture of the opponent's fleet.

When all of the squares of a ship have been hit, the ship's owner announces the sinking of the Carrier, 
Submarine, Cruiser/Destroyer/Patrol Boat, or the titular Battleship. If all of a player's ships have been 
sunk, the game is over and their opponent wins. \n"""
        messagebox.showinfo("Game Rules", rules)

    def exit_game(self):
        self.master.destroy()

def start_gui():
    root = tk.Tk()
    BattleshipGUI(root)
    root.mainloop()

#start_gui()