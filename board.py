

class Board():

    def __init__(self):
        """ Create the initial (empty) board, a matrix of 6 rows and 7 columns.
        During the game, its values can be:
            0 for a free cell
            1 for a cell occupied by a coin of player1
            -1 for a cell occupied by a coin of player2
        """
        self.board = [[0] * 7 for _ in range(6)]

    def _modify_board(self, row, column, value):
        """ Modify the board by updating the value of a specific cell (given by row, column)."""
        self.board[row][column] = value

    def get_column(self, col_number):
        """ Returns all the values on a specific column.
        """
        return [self.board[row][col_number] for row in range(6)]

    def get_row(self, row_number):
        """ Returns all the values on a specific row in a list.
        NOT USED, BUT SHOULD BE USEFUL LATER"""
        return self.board[row_number]

    def get_diagonal(self, diag_number, direction='right'):
        """ Returns all the values on a specific diagonal, defined by the diag_number (=0,...,6) and the direction (=right or left).
        The Nth diagonal is the diagonal that starts on the first row and Nth column, and goes to the left or right.
        NOT USED, BUT SHOULD BE USEFUL LATER"""
        diagonal = list()
        if direction == 'right':
            for i in range(min(6 - diag_number + 1, 6)):
                diagonal.append(self.board[i][diag_number + i])
        else:
            for i in range(min(diag_number + 1, 6)):
                diagonal.append(self.board[i][diag_number - i])
        return diagonal

    def insert_coin(self, column, value):
        """ Update the board by inserting a coin of a given value in a given column.
        Return True if the coin was added to the board.
        Return False if the coin couldn't be added to the board"""
        column_values = self.get_column(column)
        if 0 in column_values:
            free_row = column_values.index(0)
            self._modify_board(free_row, column, value)
            return True
        else:
            return False

    def __repr__(self):
        # TO IMPROVE
        return "\n".join([" ".join(format_3chars(v) for v in self.board[5 - row]) for row in range(6)])


def format_3chars(v):
    if v < 0:
        return "-1 "
    elif v == 0:
        return " 0 "
    elif v == 1:
        return " 1 "
    else:
        return " - "

        

