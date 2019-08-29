from board import Board
from players import Player_AI_Random, Player_Human, Player_AI_NN, Player_AI_MiniMax
from helpers import congratulate

board = Board()

player1 = Player_AI_MiniMax(1)
player2 = Player_AI_MiniMax(-1)

player_to_play = player1

for _ in range(42):

    # Invite the next player to play
    player_to_play.make_a_move(board)

    # Check if the game is won
    is_a_win, winner = board.is_winning_position()
    if is_a_win:
        print(board)
        if player_to_play.player_type == "Human":
            congratulate(player_to_play.name)
        else:
            print("Pffft! Looser!")
            print("%s won!" % (player_to_play.name))
        break
    else:
        player_to_play = player2 if player_to_play == player1 else player1
