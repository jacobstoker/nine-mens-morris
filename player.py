from dataclasses import dataclass
from enum import Enum, auto
from ui import UI
from type import Coord


class PlayerStates(Enum):
    PLACING = auto()
    MOVING = auto()
    FLYING_TIME = auto()
    LOST = auto()


@dataclass
class Player:
    name: str
    ui: UI
    pieces_to_place: int = 9
    pieces_on_board: int = 0
    state: PlayerStates = PlayerStates.PLACING

    def get_place_coord(self) -> Coord:
        return self.ui.get_player_place(self.name)

    def get_move_coords(self) -> list[Coord]:
        return self.ui.get_player_move(self.name)

    def get_remove_coord(self) -> Coord:
        return self.ui.get_player_remove(self.name)

    def placed_piece(self):
        """Update the counters and change the state of the player when a piece is placed"""
        if self.state == PlayerStates.PLACING:
            self.pieces_to_place -= 1
            self.pieces_on_board += 1
            if self.pieces_to_place == 0:
                self.state = PlayerStates.MOVING
        else:
            raise NotImplementedError(
                "ERROR: Called placed_piece method outside of the PLACING state. This should not be hit."
            )

    def lost_piece(self):
        """Decrement the pieces_on_board count when a piece is removed, and change the state accordingly"""
        self.pieces_on_board -= 1
        if not self.state == PlayerStates.PLACING:
            if self.pieces_on_board == 3:
                self.state = PlayerStates.FLYING_TIME
            elif self.pieces_on_board == 2:
                self.state = PlayerStates.LOST

    def __repr__(self):
        return f"Name: {self.name}, State: {self.state}, Pieces to place: {self.pieces_to_place}, Pieces on board: {self.pieces_on_board}"
