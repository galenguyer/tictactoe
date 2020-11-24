"""
A simple Tic Tac Toe game in Python
"""

BOARD = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def main():
    """
    Entrypoint for the program
    """
    print_board()


def print_board():
    """
    Prints the current state of the board
    """
    print(' {} | {} | {} '.format(BOARD[0][0], BOARD[0][1], BOARD[0][2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(BOARD[1][0], BOARD[1][1], BOARD[1][2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(BOARD[2][0], BOARD[2][1], BOARD[2][2]))


if __name__ == '__main__':
    main()
