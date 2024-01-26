from dataclasses import dataclass
from board import Board
from player import Player, PlayerStates
from ui import UI


@dataclass
class Game:
    board: Board
    player_1: Player
    player_2: Player
    ui: UI

    def place_piece(self, current_player: Player) -> None:
        """Place a piece on the board for the current player"""
        while True:
            coord = current_player.get_place_coord()

            if not self.board.valid_piece(coord):
                self.ui.notify_not_on_board(coord)
                continue

            if not self.board.empty_piece(coord):
                self.ui.notify_non_empty(coord)
                continue

            self.board.place_piece(coord, current_player.name)
            current_player.placed_piece()
            if self.board.is_part_of_mill(coord):
                self.display_board()
                self.ui.notify_mill(current_player.name)
                self.remove_piece(current_player)
            return

    def move_piece(self, current_player: Player) -> None:
        """Move a piece on the board for the current player"""
        if current_player.state == PlayerStates.LOST:
            return

        while True:
            start_coord, end_coord = current_player.get_move_coords()

            if not self.board.valid_piece(start_coord):
                self.ui.notify_not_on_board(start_coord)
                continue

            if not self.board.valid_piece(end_coord):
                self.ui.notify_not_on_board(end_coord)
                continue

            if not self.board.piece_owned_by_player(start_coord, current_player.name):
                self.ui.notify_wrong_ownership(current_player.name)
                continue

            if not self.board.empty_piece(end_coord):
                self.ui.notify_non_empty(end_coord)
                continue

            if (
                not self.board.valid_move(start_coord, end_coord)
                and current_player.state != PlayerStates.FLYING_TIME
            ):
                self.ui.notify_illegal_move(start_coord, end_coord)
                continue

            self.board.move_piece(start_coord, end_coord)
            if self.board.is_part_of_mill(end_coord):
                self.ui.notify_mill(current_player.name)
                self.remove_piece(current_player)
            return

    def remove_piece(self, current_player: Player):
        """Remove a piece on the board from the other player"""
        other_player = (
            self.player_2 if current_player is self.player_1 else self.player_1
        )

        while True:
            coord = current_player.get_remove_coord()

            if not self.board.valid_piece(coord):
                self.ui.notify_not_on_board(coord)
                continue

            if self.board.piece_owned_by_player(coord, current_player.name):
                self.ui.notify_delete_own_piece()
                continue

            if self.board.empty_piece(coord):
                self.ui.notify_delete_empty(coord)
                continue

            if self.board.is_part_of_mill(coord):
                self.ui.notify_delete_mill(coord)
                continue

            self.board.remove_piece(coord)
            other_player.lost_piece()
            return

    def display_board(self):
        """Pass the state of the game to the UI for it to display"""
        self.ui.display_current_board(
            self.board.pieces,
            self.player_1.name,
            self.player_1.pieces_to_place,
            self.player_1.pieces_on_board,
            self.player_2.name,
            self.player_2.pieces_to_place,
            self.player_2.pieces_on_board,
        )
