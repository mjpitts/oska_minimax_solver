import math
import copy


class Board:

    def __init__ (self, size):
        self.pieces = []
        self.size = size 
        self.middle = math.floor(((size*2)-3)/2)

class Piece:

    def __init__(self, color, position):
        self.color = color
        self.position = position

"""Returns a list of all the possible boards that could be generate from all the possible moves"""
def move_pieces(board, turn):
    
    new_boards = []
    positions = {}

    for piece in board.pieces:
        positions[(piece.position[0] , piece.position[1])] = piece.color

    for i, piece in enumerate(board.pieces):
        
        

        piece_copy_left = copy.deepcopy(board.pieces)
        piece_copy_right = copy.deepcopy(board.pieces)
        #move rules for pieces
        if(piece_copy_left[i].color == 'b' and turn == 'b'):
            #move left if not at the leftside of the board
            if piece_copy_left[i].position[1] != 0:
                #check if at top of board
                if(piece_copy_left[i].position[0] != 0 and not (piece_copy_left[i].position[0] - 1 , piece_copy_left[i].position[1] - 1) in positions):
                    piece_copy_left[i].position[1] -= 1
                    piece_copy_left[i].position[0] -= 1
                    new_boards.append(build_board(piece_copy_left, board.size))

            
            #move right if not at the rightside of the board
            if(piece_copy_right[i].position[1] != rowsize(piece_copy_left[i], board)):
                #check if at top of board
                if(piece_copy_right[i].position[0] != 0 and not (piece_copy_right[i].position[0] - 1 , piece_copy_right[i].position[1]) in positions):
                    piece_copy_right[i].position[1] += 0
                    piece_copy_right[i].position[0] -= 1
                    new_boards.append(build_board(piece_copy_right, board.size))
  
        #move rules for white pieces
        if(piece_copy_left[i].color == 'w' and turn == 'w'):
            #move left if not at the leftside of the board
            if(piece_copy_left[i].position[1] != 0):
               
               # check if at bottom of board and if target space is occupied
               if(piece_copy_left[i].position[0] != (board.size*2)-3 and not (piece_copy_left[i].position[0] + 1 , piece_copy_left[i].position[1] - 1) in positions):

                    piece_copy_left[i].position[1] -= 1
                    piece_copy_left[i].position[0] += 1
                    new_boards.append(build_board(piece_copy_left, board.size))
            
            #move right if not at the rightside of the board
            if(piece_copy_right[i].position[1] != rowsize(piece_copy_left[i], board)):  
               #check if at bottom of board and if target space is occupied
               if(piece_copy_right[i].position[0] != (board.size*2)-3 and not (piece_copy_right[i].position[0] + 1 , piece_copy_right[i].position[1]) in positions):
                    
                    piece_copy_right[i].position[1] += 0
                    piece_copy_right[i].position[0] += 1
                    new_boards.append(build_board(piece_copy_right, board.size))

    return new_boards
        
"""Generates a piece's current row size given the pieces row and the size of the board it occupies"""
def rowsize(piece, board):
    row = piece.position[0]
    mid = board.middle

    return(abs(row - mid) + 2)


""""Build board from a piece list.
    Returns board described by the piece list."""
def build_board(piece_list, size):
    new_board = Board(size)
    new_board.pieces = piece_list

    return new_board

""""Generate a board from a list of strings called board list.
    Returns a board from those strings"""
def generate_board(board_list):
    piece_list = []

    for i, row in enumerate(board_list):
        for column, char in enumerate(row[0: len(row) : 1]):
            if(char == 'w' or char == 'b'):
                piece_list.append(Piece(char, [i, column]))

    size = (len(board_list)+3)/2

    return build_board(piece_list, size)

"""Take in a board and print the user frienldy view of a board"""
def print_board(board):

    num_rows = int((board.size*2)-3)
    mid = board.middle
    positions = {}

    for piece in board.pieces:
        positions[(piece.position[0],piece.position[1])] = piece.color


    for row in range(num_rows):
        print_row = ""
        row_size = abs(row - mid) + 2

        for column in range(row_size):
            if (row, column) in positions:
                print_row += positions[(row,column)]
            else:
                print_row += "-"


        print(print_row)
