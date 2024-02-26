chess_file = input()

def file_check (a_file):
    try:
        file = open(chess_file, "r")
    except FileNotFoundError:
        exit()


