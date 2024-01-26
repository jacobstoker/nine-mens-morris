from type import Coord
from dataclasses import dataclass, field
from ui import UI

VALID_COORDS = [
    ("A", 1),
    ("A", 4),
    ("A", 7),
    ("B", 2),
    ("B", 4),
    ("B", 6),
    ("C", 3),
    ("C", 4),
    ("C", 5),
    ("D", 1),
    ("D", 2),
    ("D", 3),
    ("D", 5),
    ("D", 6),
    ("D", 7),
    ("E", 3),
    ("E", 4),
    ("E", 5),
    ("F", 2),
    ("F", 4),
    ("F", 6),
    ("G", 1),
    ("G", 4),
    ("G", 7),
]


def empty_board():
    """Return an empty dictionary of coords"""
    return {coord: "EMPTY" for coord in VALID_COORDS}


@dataclass
class Board:
    ui: UI
    pieces: dict = field(default_factory=empty_board)

    def piece(self, coord: Coord) -> str:
        """Return the value of the piece at the given coordiante"""
        return self.pieces[coord]

    def empty_piece(self, coord: Coord) -> bool:
        """Return whether the coordinate represents an empty piece on the board"""
        return self.pieces[coord] == "EMPTY"

    def piece_owned_by_player(self, coord: Coord, player_name: str) -> bool:
        """Return whether the piece at a given coordinate is owned by player_name"""
        return self.pieces[coord] == player_name

    def place_piece(self, coord: Coord, player_name: str) -> None:
        """Place a piece on the board at the given coordinate"""
        self.pieces[coord] = player_name
        self.ui.notify_placed_piece(coord)

    def remove_piece(self, coord: Coord) -> None:
        self.pieces[coord] = "EMPTY"
        self.ui.notify_removed_piece(coord)

    def move_piece(self, start_coord: Coord, end_coord: Coord) -> None:
        """Move a piece from a given start_coord to end_coord"""
        self.pieces[end_coord] = self.pieces[start_coord]
        self.pieces[start_coord] = "EMPTY"
        self.ui.notify_successful_move(start_coord, end_coord)

    def is_part_of_mill(self, coord: Coord) -> bool:
        x, y = coord

        vertical_coords = [(x, y) for x_coord, y in VALID_COORDS if x_coord == x]
        horizontal_coords = [(x, y) for x, y_coord in VALID_COORDS if y_coord == y]

        # Handle the special cases of the split vertical and horizontal lines
        if x == "D":
            if y in [1, 2, 3]:
                vertical_coords = [("D", 1), ("D", 2), ("D", 3)]
            else:
                vertical_coords = [("D", 5), ("D", 6), ("D", 7)]
        elif y == 4:
            if x in ["A", "B", "C"]:
                horizontal_coords = [("A", 4), ("B", 4), ("C", 4)]
            else:
                horizontal_coords = [("E", 4), ("F", 4), ("G", 4)]

        if all(
            self.piece(coord) == self.piece(vertical_coords[0])
            and self.piece(coord) != "EMPTY"
            for coord in vertical_coords
        ):
            return True

        if all(
            self.piece(coord) == self.piece(horizontal_coords[0])
            and self.piece(coord) != "EMPTY"
            for coord in horizontal_coords
        ):
            return True

        return False

    @staticmethod
    def valid_move(start_coord: Coord, end_coord: Coord) -> bool:
        """Return a bool for whether a given move is valid"""
        start_letter, start_number = start_coord
        end_letter, end_number = end_coord

        if start_letter in ["A", "G"] or start_number in [1, 7]:
            max_difference = 3
        elif start_letter in ["B", "F"] or start_number in [2, 6]:
            max_difference = 2
        else:
            max_difference = 1

        letter_diff = abs(ord(start_letter) - ord(end_letter))
        number_diff = abs(start_number - end_number)
        return (letter_diff == 0 and number_diff == max_difference) or (
            letter_diff == max_difference and number_diff == 0
        )

    @staticmethod
    def valid_piece(coord: Coord) -> bool:
        """Return whether the coordinate represents a valid location on the board"""
        return coord in VALID_COORDS
