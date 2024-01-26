from type import Coord
import os

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class CLI:
    def start_game(self):
        print("Welcome to Nine Men's Morris")

    def display_empty_board(self):
        print(
            """          
        7  o--------------o--------------o
           |              |              |
        6  |    o---------o---------o    |
           |    |         |         |    |
        5  |    |    o----o----o    |    |
           |    |    |         |    |    |
        4  o----o----o         o----o----o
           |    |    |         |    |    |
        3  |    |    o----o----o    |    |
           |    |         |         |    |
        2  |    o---------o---------o    |
           |              |              |
        1  o--------------o--------------o
           A    B    C    D    E    F    G
        """
        )

    def display_current_board(
        self,
        pieces: dict,
        player_1_name: str,
        player_1_pieces_to_place: int,
        player_1_pieces_on_board,
        player_2_name: str,
        player_2_pieces_to_place: int,
        player_2_pieces_on_board: int,
    ):
        current_pieces = {
            key: RED + player_1_name[0].upper() + RESET
            if value == player_1_name
            else GREEN + player_2_name[0].upper() + RESET
            if value == player_2_name
            else "o"
            for key, value in pieces.items()
        }

        p1_pieces_to_place = f"{RED}{"J" * player_1_pieces_to_place}{RESET}"
        p2_pieces_to_place = f"{GREEN}{"D" * player_2_pieces_to_place}{RESET}"

        p1_pieces_on_board = f"{RED}{"J" * player_1_pieces_on_board}{RESET}"
        p2_pieces_on_board = f"{GREEN}{"D" * player_2_pieces_on_board}{RESET}"

        current_board = f"""          
        7  {current_pieces[("A", 7)]}--------------{current_pieces[("D", 7)]}--------------{current_pieces[("G", 7)]}      Pieces to place
           |              |              |      {player_1_name}: {p1_pieces_to_place}
        6  |    {current_pieces[("B", 6)]}---------{current_pieces[("D", 6)]}---------{current_pieces[("F", 6)]}    |      {player_2_name}: {p2_pieces_to_place}
           |    |         |         |    |
        5  |    |    {current_pieces[("C", 5)]}----{current_pieces[("D", 5)]}----{current_pieces[("E", 5)]}    |    |      Pieces on board
           |    |    |         |    |    |      {player_1_name}: {p1_pieces_on_board}
        4  {current_pieces[("A", 4)]}----{current_pieces[("B", 4)]}----{current_pieces[("C", 4)]}         {current_pieces[("E", 4)]}----{current_pieces[("F", 4)]}----{current_pieces[("G", 4)]}      {player_2_name}: {p2_pieces_on_board}
           |    |    |         |    |    |
        3  |    |    {current_pieces[("C", 3)]}----{current_pieces[("D", 3)]}----{current_pieces[("E", 3)]}    |    |
           |    |         |         |    |
        2  |    {current_pieces[("B", 2)]}---------{current_pieces[("D", 2)]}---------{current_pieces[("F", 2)]}    |
           |              |              |
        1  {current_pieces[("A", 1)]}--------------{current_pieces[("D", 1)]}--------------{current_pieces[("G", 1)]}
           A    B    C    D    E    F    G
        """
        clear_screen()
        print(current_board)

    def get_player_name(self, player_number: int) -> str:
        return input(f"{player_number}- Enter name: ")

    def get_player_place(self, player_name: str) -> Coord:
        coord_input = input(f"{player_name}- Enter a coordinate to place: ")
        letter, number = coord_input[0], int(coord_input[1])
        return (letter, number)

    def get_player_move(self, player_name: str) -> list[Coord]:
        coord_input = input(f"{player_name}- Enter a coordinate to move from: ")
        start_coord: Coord = (coord_input[0], int(coord_input[1]))
        coord_input = input(f"{player_name}- Enter a coordinate to move to: ")
        end_coord: Coord = (coord_input[0], int(coord_input[1]))
        return [start_coord, end_coord]

    def get_player_remove(self, player_name: str) -> Coord:
        coord_input = input(f"{player_name}- Enter piece to remove: ")
        letter, number = coord_input[0], int(coord_input[1])
        return (letter, number)

    def notify_placed_piece(self, coord: Coord):
        print(f"NOTE: Placed piece at {coord}")

    def notify_illegal_place(self, coord: Coord):
        print(f"ERROR: Can't place piece at {coord}")

    def notify_removed_piece(self, coord: Coord):
        print(f"NOTE: Removed piece at {coord}")

    def notify_illegal_move(self, start_coord: Coord, end_coord: Coord):
        print(f"ERROR: Illegal move {start_coord} -> {end_coord}!!")

    def notify_successful_move(self, start_coord: Coord, end_coord: Coord):
        print(f"NOTE: Moved {start_coord} -> {end_coord}")

    def notify_mill(self, player_name: str):
        print(f"{player_name} - MILL!")

    def notify_wrong_ownership(self, owner: str):
        print(f"ERROR: Piece is not occupied by {owner}!")

    def notify_delete_own_piece(self):
        print("ERROR: You can't delete your own piece!")

    def announce_winner(self, winning_player: str):
        print(f"Player {winning_player} wins!")
    
    def notify_non_empty(self, coord: Coord):
        print(f"ERROR: {coord} is not empty!")
    
    def notify_not_on_board(self, coord: Coord):
        print(f"ERROR: {coord} is not even on the board!")

    def notify_delete_mill(self, coord: Coord):
        print(f"ERROR: Can't remove {coord}, it's part of a mill!")

    def notify_delete_empty(self, coord: Coord):
        print(f"ERROR: Can't remove {coord}, it's empty!")


# interface = CLI()
# interface.display_board()
# thing = interface.get_player_move()
# print(thing)
