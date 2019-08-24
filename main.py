from board import Board
from players import Player_AI_Random, Player_Human

board = Board()

player1 = Player_Human(1)
player2 = Player_AI_Random(-1)

player_to_play = player1

for _ in range(42):

    # Invite the next player to play
    player_to_play.make_a_move(board)

    # Check if the game is won
    if board.winning_position():
        print(board)
        if player_to_play.player_type == "Human":
            print("Congratulation %s, you won!" % (player_to_play.name))
        else:
            print("Pffft! Looser!")
        break
    else:
        player_to_play = player2 if player_to_play == player1 else player1
