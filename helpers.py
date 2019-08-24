import subprocess


def congratulate(player_name):
    subprocess.check_call(['cowsay', "CONGRATULATIONS %s !!!" % (player_name)])


def clear_screen():
    subprocess.check_call(["clear"])
