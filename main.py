from board import Board
from cli_ui import CLI
from game import Game
from player import Player, PlayerStates


def main():
    ui = CLI()
    board = Board(ui)

    ui.start_game()
    player_1 = Player(name=ui.get_player_name(1), ui=ui)
    player_2 = Player(name=ui.get_player_name(2), ui=ui)
    game = Game(board, player_1, player_2, ui)

    while (
        player_1.state == PlayerStates.PLACING or player_2.state == PlayerStates.PLACING
    ):
        game.display_board()
        game.place_piece(player_1)
        game.display_board()
        game.place_piece(player_2)

    while player_1.state != PlayerStates.LOST and player_2.state != PlayerStates.LOST:
        game.display_board()
        game.move_piece(player_1)
        game.display_board()
        game.move_piece(player_2)

    if player_1.state == PlayerStates.LOST:
        ui.announce_winner(player_2.name)
    elif player_2.state == PlayerStates.LOST:
        ui.announce_winner(player_1.name)


if __name__ == "__main__":
    main()
