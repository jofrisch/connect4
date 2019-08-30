from random import choice
import copy
#from model.cnn_definition import First_CNN
#from model.make_prediction import predict_chance_to_win
from helpers import minimax


class Player_AI_Random():

    def __init__(self, value):
        self.player_value = value
        self.name = "AI player"
        self.player_type = "AI"

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        opened_columns = board.get_opened_columns()
        selected_column = choice(opened_columns)
        print("AI player plays in column: %i" % (selected_column + 1))
        return board.insert_coin(selected_column, self.player_value)


class Player_AI_NN():

    def __init__(self, value):
        self.player_value = value
        self.name = "AI NN player"
        self.player_type = "AI"
        self.cnn = First_CNN.build()

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        max_chance = 0
        for column in board.get_opened_columns():
            tmp_board = copy.deepcopy(board)
            tmp_board.insert_coin(column, self.player_value)
            chance = predict_chance_to_win(tmp_board.board, self.cnn)
            print(column + 1, chance)
            if chance >= max_chance:
                max_chance = chance
                best_column = column

        print("AI NN player plays in column: %i" % (best_column + 1))
        return board.insert_coin(best_column, self.player_value)


class Player_Human():

    def __init__(self, coin_value):
        self.coin_value = coin_value
        self.name = input("What is your name?\n")
        self.player_type = "Human"

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        print(board)

        call = input("Please choose a column: ")
        valid_call = call in list("1234567") and board.insert_coin(int(call) - 1, self.coin_value)

        while not valid_call:
            print("Impossible move!")
            print("Please enter a column number (1 to 7), where there is an available spot.")
            call = input("> ")
            valid_call = call in list("1234567") and board.insert_coin(int(call) - 1, self.coin_value)

class Player_AI_MiniMax():

    def __init__(self, value):
        self.player_value = value
        self.name = "AI Minimax player"
        self.player_type = "AI"

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        tmp_board = copy.deepcopy(board)
        best_col, score = minimax(tmp_board, 5, self.player_value)
        print("AI Minimax player plays in column: %i" % (best_col + 1))
        return board.insert_coin(best_col, self.player_value)
