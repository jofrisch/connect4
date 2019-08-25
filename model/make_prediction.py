from helpers import convert_2Dmatrix_to_np
import numpy as np


def predict_chance_to_win(board, cnn):
    """ Predict the chance to win."""
    # Reshape the board
    board = np.array(convert_2Dmatrix_to_np([board])).reshape((6, 7, 1))
    board = np.expand_dims(board, axis=0)
    return cnn.predict(board)[0][0]
