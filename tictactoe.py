"""
A simple Tic Tac Toe game in Python
"""

def main():
    """
    Entrypoint for the program
    """
    print_board()


def print_board():
    """
    Prints the current state of the board
    """
    print('{:3}|{:3}|{:3}'.format(' ', ' ', ' '))
    print('---+---+---')
    print('{:3}|{:3}|{:3}'.format(' ', ' ', ' '))
    print('---+---+---')
    print('{:3}|{:3}|{:3}'.format(' ', ' ', ' '))


if __name__ == '__main__':
    main()
