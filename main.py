import math
import classes

def main():
    # board = classes.generate_board(['wwww', '---', '--', '---', 'bbbb'])
    # new_states = classes.move_pieces(board, 'w')

    # for state in new_states:
    #     classes.print_board(state)
    #     print()

    board = classes.oskaplayer(['---w', '---', 'bb', '--w', '----'], 'w', 2)
    
    print(board)

if __name__ == '__main__':
    main()

