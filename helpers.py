import subprocess
import numpy as np
from random import random
import cowsay

def congratulate(player_name):
    cowsay.cow("CONGRATULATIONS %s !!!" % (player_name))


def clear_screen():
    subprocess.check_call(["clear"])


def flatten(matrix):
    return [item for sublist in matrix for item in sublist]


def convert_2Dmatrix_to_np(matrix):
    return np.array([np.array(row) for row in matrix])


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def minimax(board, depth, coin, player=1):
    """ Run the minimax algorithm.
    If player == 1 (resp. -1) you want to maximize (resp. minimize) the gain.
    WE MUST MAKE SURE THAT depth IS < NB OF MOVES REMAINING
    """
    if player == 1:
        best = [-1, -1000]  # best = [column_id_to_play, score]
    else:
        best = [-1, 1000]

    is_a_win, _ = board.is_winning_position()
    if depth == 0 or is_a_win:
        score = evaluate(board, coin, depth)
        return [-1, score]

    for column in board.get_opened_columns():
        board.insert_coin(column, coin)
        score = minimax(board, depth - 1, -coin, player=-player)
        board.undo_move(column)
        score[0] = column

        if player == 1:
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score

    return best


def evaluate(board, coin, depth):
    is_a_win, winner = board.is_winning_position()
    if is_a_win and winner == coin:
        return 1 + random() * 0.01 + depth * 0.1
    elif is_a_win and winner != coin:
        return - (1 + random() * 0.01 + depth * 0.1)
    else:
        return random() * 0.3
