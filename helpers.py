import subprocess
import numpy as np


def congratulate(player_name):
    subprocess.check_call(['cowsay', "CONGRATULATIONS %s !!!" % (player_name)])


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
