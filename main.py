import math
import classes

def main():
    board = classes.generate_board(['www-', '--w', '--', '---', 'bbbb'])
    new_states = classes.move_pieces(board, 'b')

    for state in new_states:
        classes.print_board(state)
        print()

if __name__ == '__main__':
    main()

