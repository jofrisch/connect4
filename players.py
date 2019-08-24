from random import choice


class Player_AI_Random():

    def __init__(self, value):
        self.player_value = value
        self.name = "AI player"
        self.player_type = "AI"

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        opened_columns = board.get_opened_columns()
        selected_column = choice(opened_columns)
        print("AI player plays in column: %i" % (selected_column))
        return board.insert_coin(selected_column, self.player_value)


class Player_Human():

    def __init__(self, coin_value):
        self.coin_value = coin_value
        self.name = input("What is your name?\n")
        self.player_type = "Human"

    def make_a_move(self, board):
        """ Chooses a column to insert a coin."""
        print(board)

        call = input("Please choose a column: ")
        valid_call = call in list("0123456") and board.insert_coin(int(call), self.coin_value)

        while not valid_call:
            print("Impossible move!")
            print("Please enter a column number (0 to 6), where there is an available spot.")
            call = input("> ")
            valid_call = call in list("0123456") and board.insert_coin(int(call), self.coin_value)