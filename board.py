from helpers import flatten

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
        """
        return self.board[row_number]

    def get_diagonal(self, diag_number, direction='right'):
        """ Returns all the values on a specific diagonal.
        A diagonal is defined by the diag_number (=0,...,6) and the direction (=right or left).
        The diag_number refers to the diagonal that passes through the row_id = 2 and col_id = diag_number
        """
        diagonal = list()
        if direction == 'right':
            start = max(0, 2 - diag_number)
            end = min(6, 9 - diag_number)
            for i in range(start, end):
                j = (i - 2 + diag_number) % 7
                diagonal.append(self.board[i][j])
        else:
            start = max(0, diag_number - 4)
            end = min(6, diag_number + 3)
            for i in range(start, end):
                j = (2 + diag_number - i) % 7
                diagonal.append(self.board[i][j])
        return diagonal

    def get_opened_columns(self):
        """ Returns  a list of column ids that are opened.
        A column is opened if at least the last row contains a 0."""
        return [col for col in range(7) if self.board[5][col] == 0]

    def insert_coin(self, column, value):
        """ Updates the board by inserting a coin of a given value in a given column.
        Returns True if the coin was added to the board.
        Returns False if the coin couldn't be added to the board"""
        column_values = self.get_column(column)
        if 0 in column_values:  # check if column is opened
            free_row = column_values.index(0)  # identify the first row that is empty
            self._modify_board(free_row, column, value)  # update the value on that row
            return True
        else:
            return False

    def is_winning_position(self):
        for column in range(7):
            winner = contains_4_consecutive_coins(self.get_column(column))
            if winner:
                return True, winner
        for row in range(6):
            winner = contains_4_consecutive_coins(self.get_row(row))
            if winner:
                return True, winner
        for direction in ['right', 'left']:
            for diagonal in range(7):
                winner = contains_4_consecutive_coins(self.get_diagonal(diagonal, direction))
                if winner:
                    return True, winner
        # If we couldn't find a winning position
        return False, 0

    def undo_move(self, column, row=None):
        """Replace last coin of the given column by an empty cell.
        You can provide the row to gain speed.
        """
        if row:
            self.board[row][column] = 0
        else:
            column_values = self.get_column(column)
            if column_values[-1] == 0:
                row = column_values.index(0) - 1
            else:
                row = 5
            self.board[row][column] = 0

    def __repr__(self):
        # TO IMPROVE
        header = " 1   2   3   4   5   6   7" + "\n"
        separator = "=" * 27 + "\n"
        board = "\n".join([" ".join(format_3chars(v) for v in self.board[5 - row]) for row in range(6)])
        return header + separator + board


def format_3chars(v):
    if v == -1:
        return " X "
    elif v == 0:
        return " - "
    elif v == 1:
        return " 0 "
    else:
        return "   "


def contains_4_consecutive_coins(values):
    """
    Return 0 if there are no 4 consecutive rows, return the coin value of the 4 otherwise.
    """
    size = len(values)
    if size < 4:
        return 0
    else:
        for i in range(size - 3):
            if sum(values[i: i + 4]) == 4:
                return 1
            elif sum(values[i: i + 4]) == -4:
                return -1
        return 0





