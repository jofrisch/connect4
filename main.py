from board import Board
from players import Player_AI_Random, Player_Human, Player_AI_NN, Player_AI_MiniMax
from helpers import congratulate, check_save_board, store_saved_boards
from random import randint, choice

for _ in range(20000):
    board = Board()

    if choice([True, False]):
        player1 = Player_AI_MiniMax(1)
        player2 = Player_AI_Random(-1)
    else:
        player1 = Player_AI_Random(1)
        player2 = Player_AI_MiniMax(-1)

    player_to_play = player1

    saved_boards = []
    saves_seed = randint(0, 5)

    for move in range(42):

        # Invite the next player to play
        player_to_play.make_a_move(board)

        # Check if the game is won
        is_a_win, winner = board.is_winning_position()
        if is_a_win:

            print(board)

            # Save the board
            saved_boards.append(board.board)

            # Close the game by sending a message
            if player_to_play.player_type == "Human":
                congratulate(player_to_play.name)
            else:
                print("%s won!" % (player_to_play.name))
            break

        else:
            # Switch players for the next move
            player_to_play = player2 if player_to_play == player1 else player1

            # Check to save the board
            check_save_board(saved_boards, board.board, move, saves_seed)

    store_saved_boards(saved_boards, winner)
