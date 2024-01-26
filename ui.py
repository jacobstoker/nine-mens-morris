from typing import Protocol
from type import Coord


class UI(Protocol):
    def start_game(self):
        raise NotImplementedError

    def display_empty_board(self):
        raise NotImplementedError

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
        raise NotImplementedError

    def get_player_name(self, player_number: int) -> str:
        raise NotImplementedError

    def notify_placed_piece(self, coord: Coord):
        raise NotImplementedError

    def notify_illegal_place(self, coord: Coord):
        raise NotImplementedError

    def notify_removed_piece(self, coord: Coord):
        raise NotImplementedError

    def get_player_place(self, player_name: str) -> Coord:
        raise NotImplementedError

    def get_player_move(self, player_name: str) -> list[Coord]:
        raise NotImplementedError

    def get_player_remove(self, player_name: str) -> Coord:
        raise NotImplementedError

    def notify_illegal_move(self, start_coord: Coord, end_coord: Coord):
        raise NotImplementedError

    def notify_successful_move(self, start_coord: Coord, end_coord: Coord):
        raise NotImplementedError

    def notify_mill(self, player_name: str):
        raise NotImplementedError

    def announce_winner(self, winning_player: str):
        raise NotImplementedError

    def notify_wrong_ownership(self, owner: str):
        raise NotImplementedError

    def notify_delete_own_piece(self):
        raise NotImplementedError

    def notify_non_empty(self, coord: Coord):
        raise NotImplementedError

    def notify_not_on_board(self, coord: Coord):
        raise NotImplementedError

    def notify_delete_mill(self, coord: Coord):
        raise NotImplementedError

    def notify_delete_empty(self, coord: Coord):
        raise NotImplementedError
