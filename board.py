

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
        """ Returns all the values on a specific diagonal, defined by the diag_number (=0,...,6) and the direction (=right or left).
        The Nth diagonal is the diagonal that starts on the first row and Nth column, and goes to the left or right.
        """
        diagonal = list()
        if direction == 'right':
            for i in range(min(6 - diag_number + 1, 6)):
                diagonal.append(self.board[i][diag_number + i])
        else:
            for i in range(min(diag_number + 1, 6)):
                diagonal.append(self.board[i][diag_number - i])
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
            if contains_4_consecutive_coins(self.get_column(column)):
                return True
        for row in range(6):
            if contains_4_consecutive_coins(self.get_row(row)):
                return True
        for direction in ['right', 'left']:
            for diagonal in range(7):
                if contains_4_consecutive_coins(self.get_diagonal(diagonal, direction)):
                    return True
        # If we couldn't find a winning position
        return False

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
                row = 6
            self.board[row][column] = 0

    def __repr__(self):
        # TO IMPROVE
        header = " 1   2   3   4   5   6   7" + "\n"
        separator = "=" * 27 + "\n"
        board = "\n".join([" ".join(format_3chars(v) for v in self.board[5 - row]) for row in range(6)])
        return header + separator + board


def format_3chars(v):
    if v < 0:
        return " X "
    elif v == 0:
        return " - "
    elif v == 1:
        return " 0 "
    else:
        return "   "


def contains_4_consecutive_coins(values):
    size = len(values)
    if size < 4:
        return False
    else:
        for i in range(size - 3):
            if sum(values[i: i + 4]) == 4 or sum(values[i: i + 4]) == -4:
                return True
        return False


if __name__ == "__main__":

    board = Board()
    print(board)

    player = 0

    for _ in range(42):

        coin = (-1)**player  # Coin = 1 for player1, -1 for player 2

        # Invite the next player to play; if the move is valid, update the board
        call = input("Player %i to play... " % (player + 1))
        valid_call = call in list("0123456") and board.insert_coin(int(call), coin)

        while not valid_call:
            print("Please enter a column number (from 0 to 6), where there is an available spot.")
            call = input("Player %i to play... " % (player + 1))
            valid_call = call in list("0123456") and board.insert_coin(int(call), coin)

        # Check if the game is won
        if board.winning_position():
            print(board)
            print("Congratulation player %i, you won!" % (player + 1))
            break
        else:
            player = (player + 1) % 2
            print(board)




