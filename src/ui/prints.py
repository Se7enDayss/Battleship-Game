from colorama import Fore


class PrintMessages:
    def welcome(self):
        print(
Fore.LIGHTBLUE_EX + '.' * 117 + """ 
 ____       _      _____   _____   _       _____   ____    _   _   ___   ____        ____      _      __  __   _____ 
| __ )     / \    |_   _| |_   _| | |     | ____| / ___|  | | | | |_ _| |  _ \      / ___|    / \    |  \/  | | ____|
|  _ \    / _ \     | |     | |   | |     |  _|   \___ \  | |_| |  | |  | |_) |    | |  _    / _ \   | |\/| | |  _|  
| |_) |  / ___ \    | |     | |   | |___  | |___   ___) | |  _  |  | |  |  __/     | |_| |  / ___ \  | |  | | | |___ 
|____/  /_/   \_\   |_|     |_|   |_____| |_____| |____/  |_| |_| |___| |_|         \____| /_/   \_\ |_|  |_| |_____|        
""" +'.' * 117 + Fore.RESET)

    def options(self):
        print(Fore.MAGENTA + """
[1] START GAME
[2] READ RULES
[3] EXIT
        """ + Fore.RESET)
    def ship_requirements(self):
        print(Fore.CYAN+"You need to place 5 ships on the board:"+Fore.RESET)
        print(Fore.CYAN+"   -> Carrier : 5 cells"+Fore.RESET)
        print(Fore.CYAN+"   -> Battleship : 4 cells"+Fore.RESET)
        print(Fore.CYAN+"   -> Destroyer : 3 cells"+Fore.RESET)
        print(Fore.CYAN+"   -> Submarine : 3 cells"+Fore.RESET)
        print(Fore.CYAN+"   -> Patrol Boat : 2 cells\n"+Fore.RESET)
    def rules(self):
        print(Fore.RED+"\nRules:"+Fore.RESET)
        print("""
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
sunk, the game is over and their opponent wins. \n""")

    def won(self):
        print(Fore.GREEN+"""
  ____                                          _             _           _     _                         _     __   __                                                _ 
 / ___|   ___    _ __     __ _   _ __    __ _  | |_   _   _  | |   __ _  | |_  (_)   ___    _ __    ___  | |    \ \ / /   ___    _   _     __      __   ___    _ __   | |
| |      / _ \  | '_ \   / _` | | '__|  / _` | | __| | | | | | |  / _` | | __| | |  / _ \  | '_ \  / __| | |     \ V /   / _ \  | | | |    \ \ /\ / /  / _ \  | '_ \  | |
| |___  | (_) | | | | | | (_| | | |    | (_| | | |_  | |_| | | | | (_| | | |_  | | | (_) | | | | | \__ \ |_|      | |   | (_) | | |_| |     \ V  V /  | (_) | | | | | |_|
 \____|  \___/  |_| |_|  \__, | |_|     \__,_|  \__|  \__,_| |_|  \__,_|  \__| |_|  \___/  |_| |_| |___/ (_)      |_|    \___/   \__,_|      \_/\_/    \___/  |_| |_| (_)
                         |___/                                                                                                                                            
"""+Fore.RESET)

    def lost(self):
        print(Fore.RED+"""
  __   __                     _                 _     _ 
  \ \ / /   ___    _   _     | |   ___    ___  | |_  | |
   \ V /   / _ \  | | | |    | |  / _ \  / __| | __| | |
    | |   | (_) | | |_| |    | | | (_) | \__ \ | |_  |_|
    |_|    \___/   \__,_|    |_|  \___/  |___/  \__| (_)
"""+Fore.RESET)

#printing=PrintMessages()
#printing.lost()


