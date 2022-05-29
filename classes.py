from math import floor
import copy


class Board:

    def __init__ (self, size):
        self.pieces = []
        self.size = size 
        self.middle = floor(((size*2)-3)/2)

class Piece:

    def __init__(self, color, position):
        self.color = color
        self.position = position

"""Returns a list of all the possible boards that could be generate from all the possible moves"""
#need to update for move_pieces to account for taking pieces
def move_pieces(board, turn):
    
    new_boards = []
    positions = {}

    for piece in board.pieces:
        positions[(piece.position[0] , piece.position[1])] = piece.color

    for i, piece in enumerate(board.pieces):
        
        target = 0

        piece_copy_left = copy.deepcopy(board.pieces)
        piece_copy_right = copy.deepcopy(board.pieces)
        
        # move black pieces
        if(piece_copy_left[i].color == 'b' and turn == 'b'):
            
            #left moves

            # check row because a piece's row determines how it views diagonality 
            if(piece_copy_left[i].position[0] > board.middle):
                # check if piece is in last column, if it is then there is no place to jump
                if(piece_copy_left[i].position[1] != 0):
                    # check if jump is empty, if empty then we will take the spot
                    if( (piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]-1) not in positions):
                       
                        piece_copy_left[i].position[0] -= 1
                        piece_copy_left[i].position[1] -= 1
                        # create new board with new left move. 
                        new_boards.append(build_board(piece_copy_left, board.size))

                    # if jump is not empty we must check if it friendly or not
                    else:
                       
                        
                        # if the piece is an enemy we must check if we can jump it or not
                        if(positions[(piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]-1)] == 'w'):
                                
                            # check if we are 1 off of mid, this changes double jump calculation 
                            if(piece_copy_left[i].position[0] > board.middle+1):
                                    
                                #first  check if we are near board bounds
                                if(piece_copy_left[i].position[1] != 1):
                                    #check if double jump space is clear
                                    if((piece_copy_left[i].position[0]-2, piece_copy_left[i].position[1]-2) not in positions):

                                        # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                        # search for jumped white piece and delete
                                        for j, piece in enumerate(piece_copy_left):
                                            if piece.position == [piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]-1]:
                                                target = j
                                                break

                                        # perform double jump 
                                        piece_copy_left[i].position[0] -= 2
                                        piece_copy_left[i].position[1] -= 2

                                        # create new board with new left move. 
                                        del piece_copy_left[target]
                                        new_boards.append(build_board(piece_copy_left, board.size))

                            # piece is too close to middle so calculation for double jump is altered
                            else:
                                    
                                #check if double jump space is clear
                                if((piece_copy_left[i].position[0]-2, piece_copy_left[i].position[1]-1) not in positions):
                                        
                                    # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_left):
                                        if piece.position == [piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]-1]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_left[i].position[0] -= 2
                                    piece_copy_left[i].position[1] -= 1

                                    # create new board with new left move. 
                                    del piece_copy_left[target]
                                    new_boards.append(build_board(piece_copy_left, board.size))
            # piece is past or on middle                  
            else:
                # check if piece is at the top of the board
                if piece_copy_left[i].position[0] != 0:

                    # check if jump is empty, if it is empty then it will take the spot
                    if( (piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]) not in positions ):
                        
                        piece_copy_left[i].position[0] -= 1
                        piece_copy_left[i].position[1] += 0
                        # create new board with new left move. 
                        new_boards.append(build_board(piece_copy_left, board.size))
                    # there is a piece in the way, so we must check if it friendly
                    else:
                        # if is was friendly then there would be no move
                        if(positions[(piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1])] == 'w'):
                            
                            # No alterations are made when above the middle deppending on distance to middle
                            #instead check if at row 1
                            if(piece_copy_left[i].position[0] != 1):
                                
                                #check if double jump space is clear
                                if((piece_copy_left[i].position[0]-2, piece_copy_left[i].position[1]) not in positions):

                                    # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_left):
                                        if piece.position == [piece_copy_left[i].position[0]-1, piece_copy_left[i].position[1]]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_left[i].position[0] -= 2
                                    piece_copy_left[i].position[1] += 0

                                    # create new board with new left move. 
                                    del piece_copy_left[target]
                                    new_boards.append(build_board(piece_copy_left, board.size))


            # right moves

            # check row because a piece's row determines how it views diagonality 
            if(piece_copy_right[i].position[0] > board.middle):
                # check if piece is in last column to the right, if it is then there is no place to jump
                if(piece_copy_right[i].position[1] != rowsize(piece_copy_right[i], board)-1):
                    # check if jump is empty, if empty then we will take the spot
                    if( (piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]) not in positions):
                       
                        piece_copy_right[i].position[0] -= 1
                        piece_copy_right[i].position[1] -= 0
                        # create new board with new right move. 
                        new_boards.append(build_board(piece_copy_right, board.size))

                    # if jump is not empty we must check if it friendly or not
                    else:

                        # if the piece is an enemy we must check if we can jump it or not
                        if(positions[(piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1])] == 'w'):
                                
                            # check if we are 1 off of mid, this changes double jump calculation 
                            if(piece_copy_right[i].position[0] > board.middle+1):
                                #check if we are near right board bound
                                if(piece_copy_right[i].position[1] != (rowsize(piece_copy_right[i], board) - 2 )):
                                    #check if double jump space is clear
                                    if((piece_copy_right[i].position[0]-2, piece_copy_right[i].position[1]) not in positions):

                                        # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                        # search for jumped white piece and delete
                                        for j, piece in enumerate(piece_copy_right):
                                            if piece.position == [piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]]:
                                                target = j
                                                break

                                        # perform double jump 
                                        piece_copy_right[i].position[0] -= 2
                                        piece_copy_right[i].position[1] -= 0

                                        # create new board with new right move. 
                                        del piece_copy_right[target]
                                        new_boards.append(build_board(piece_copy_right, board.size))

                            # piece is too close to middle so calculation for double jump is altered
                            else:
                                    
                                #check if double jump space is clear
                                if((piece_copy_right[i].position[0]-2, piece_copy_right[i].position[1]+1) not in positions):
                                        
                                    # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_right):
                                        if piece.position == [piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_right[i].position[0] -= 2
                                    piece_copy_right[i].position[1] += 1

                                    # create new board with new right move. 
                                    del piece_copy_right[target]
                                    new_boards.append(build_board(piece_copy_right, board.size))

            # piece is past or on middle                  
            else:
                # check if piece is at the top of the board
                if piece_copy_right[i].position[0] != 0:

                    # check if jump is empty, if it is empty then it will take the spot
                    if( (piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]+1) not in positions ):
                        
                        piece_copy_right[i].position[0] -= 1
                        piece_copy_right[i].position[1] += 1
                        # create new board with new right move. 
                        new_boards.append(build_board(piece_copy_right, board.size))
                    # there is a piece in the way, so we must check if it friendly
                    else:
                        # if is was friendly then there would be no move
                        if(positions[(piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]+1)] == 'w'):
                            
                            # No alterations are made when above the middle deppending on distance to middle
                            #instead check if at row 1
                            if(piece_copy_right[i].position[0] != 1):
                                
                                #check if double jump space is clear
                                if((piece_copy_right[i].position[0]-2, piece_copy_right[i].position[1]+2) not in positions):

                                    # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_right):
                                        if piece.position == [piece_copy_right[i].position[0]-1, piece_copy_right[i].position[1]+1]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_right[i].position[0] -= 2
                                    piece_copy_right[i].position[1] += 2

                                    # create new board with new right move. 
                                    del piece_copy_right[target]
                                    new_boards.append(build_board(piece_copy_right, board.size))

  
        # move rules for white pieces

        elif(piece_copy_left[i].color == 'w' and turn == 'w'):
            #left moves

            # check row because a piece's row determines how it views diagonality 
            if(piece_copy_left[i].position[0] < board.middle):
                # check if piece is in last column, if it is then there is no place to jump
                if(piece_copy_left[i].position[1] != 0):
                    # check if jump is empty, if empty then we will take the spot
                    if( (piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]-1) not in positions):
                       
                        piece_copy_left[i].position[0] += 1
                        piece_copy_left[i].position[1] -= 1
                        # create new board with new left move. 
                        new_boards.append(build_board(piece_copy_left, board.size))

                    # if jump is not empty we must check if it friendly or not
                    else:
                       
                        
                        # if the piece is an enemy we must check if we can jump it or not
                        if(positions[(piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]-1)] == 'b'):
                                
                            # check if we are 1 off of mid, this changes double jump calculation 
                            if(piece_copy_left[i].position[0] < board.middle-1):
                                    
                                #first  check if we are near board bounds
                                if(piece_copy_left[i].position[1] != 1):
                                    #check if double jump space is clear
                                    if((piece_copy_left[i].position[0]+2, piece_copy_left[i].position[1]-2) not in positions):

                                        # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                        # search for jumped white piece and delete
                                        for j, piece in enumerate(piece_copy_left):
                                            if piece.position == [piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]-1]:
                                                target = j
                                                break

                                        # perform double jump 
                                        piece_copy_left[i].position[0] += 2
                                        piece_copy_left[i].position[1] -= 2

                                        # create new board with new left move. 
                                        del piece_copy_left[target]
                                        new_boards.append(build_board(piece_copy_left, board.size))

                            # piece is too close to middle so calculation for double jump is altered
                            else:
                                    
                                #check if double jump space is clear
                                if((piece_copy_left[i].position[0]+2, piece_copy_left[i].position[1]-1) not in positions):
                                        
                                    # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_left):
                                        if piece.position == [piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]-1]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_left[i].position[0] += 2
                                    piece_copy_left[i].position[1] -= 1

                                    # create new board with new left move. 
                                    del piece_copy_left[target]
                                    new_boards.append(build_board(piece_copy_left, board.size))
            # piece is past or on middle                  
            else:
                # check if piece is at the bottom of the board
                if piece_copy_left[i].position[0] != (board.size*2)-4:

                    # check if jump is empty, if it is empty then it will take the spot
                    if( (piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]) not in positions ):
                        
                        piece_copy_left[i].position[0] += 1
                        piece_copy_left[i].position[1] += 0
                        # create new board with new left move. 
                        new_boards.append(build_board(piece_copy_left, board.size))
                    # there is a piece in the way, so we must check if it friendly
                    else:
                        # if is was friendly then there would be no move
                        if(positions[(piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1])] == 'b'):
                            
                            # No alterations are made when above the middle deppending on distance to middle
                            #instead check if at row 1
                            if(piece_copy_left[i].position[0] != (board.size*2)-5 ):
                                
                                #check if double jump space is clear
                                if((piece_copy_left[i].position[0]+2, piece_copy_left[i].position[1]) not in positions):

                                    # print(f'{piece_copy_left[i].position} {piece_copy_left[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_left):
                                        if piece.position == [piece_copy_left[i].position[0]+1, piece_copy_left[i].position[1]]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_left[i].position[0] += 2
                                    piece_copy_left[i].position[1] += 0

                                    # create new board with new left move. 
                                    del piece_copy_left[target]
                                    new_boards.append(build_board(piece_copy_left, board.size))


            # right moves

            # check row because a piece's row determines how it views diagonality 
            if(piece_copy_right[i].position[0] < board.middle):
                # check if piece is in last column to the right, if it is then there is no place to jump
                if(piece_copy_right[i].position[1] != rowsize(piece_copy_right[i], board)-1):
                    # check if jump is empty, if empty then we will take the spot
                    if( (piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]) not in positions):
                       
                        piece_copy_right[i].position[0] += 1
                        piece_copy_right[i].position[1] -= 0
                        # create new board with new right move. 
                        new_boards.append(build_board(piece_copy_right, board.size))

                    # if jump is not empty we must check if it friendly or not
                    else:

                        # if the piece is an enemy we must check if we can jump it or not
                        if(positions[(piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1])] == 'b'):
                                
                            # check if we are 1 off of mid, this changes double jump calculation 
                            if(piece_copy_right[i].position[0] < board.middle-1):
                                #check if we are near right board bound
                                if(piece_copy_right[i].position[1] != (rowsize(piece_copy_right[i], board) - 2 )):
                                    #check if double jump space is clear
                                    if((piece_copy_right[i].position[0]+2, piece_copy_right[i].position[1]) not in positions):

                                        # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                        # search for jumped white piece and delete
                                        for j, piece in enumerate(piece_copy_right):
                                            if piece.position == [piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]]:
                                                target = j
                                                break

                                        # perform double jump 
                                        piece_copy_right[i].position[0] += 2
                                        piece_copy_right[i].position[1] -= 0

                                        # create new board with new right move. 
                                        del piece_copy_right[target]
                                        new_boards.append(build_board(piece_copy_right, board.size))

                            # piece is too close to middle so calculation for double jump is altered
                            else:
                                    
                                #check if double jump space is clear
                                if((piece_copy_right[i].position[0]+2, piece_copy_right[i].position[1]+1) not in positions):
                                        
                                    # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_right):
                                        if piece.position == [piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_right[i].position[0] += 2
                                    piece_copy_right[i].position[1] += 1

                                    # create new board with new right move. 
                                    del piece_copy_right[target]
                                    new_boards.append(build_board(piece_copy_right, board.size))

            # piece is past or on middle                  
            else:
                # check if piece is at the bottom of the board
                if piece_copy_right[i].position[0] != (board.size*2)-4:

                    # check if jump is empty, if it is empty then it will take the spot
                    if( (piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]+1) not in positions ):
                        
                        piece_copy_right[i].position[0] += 1
                        piece_copy_right[i].position[1] += 1
                        # create new board with new right move. 
                        new_boards.append(build_board(piece_copy_right, board.size))
                    # there is a piece in the way, so we must check if it friendly
                    else:
                        # if is was friendly then there would be no move
                        if(positions[(piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]+1)] == 'b'):
                            
                            # No alterations are made when above the middle deppending on distance to middle
                            #instead check if at row 1
                            if(piece_copy_right[i].position[0] != (board.size*2)-5):
                                
                                #check if double jump space is clear
                                if((piece_copy_right[i].position[0]+2, piece_copy_right[i].position[1]+2) not in positions):

                                    # print(f'{piece_copy_right[i].position} {piece_copy_right[i].color}')
                                    # search for jumped white piece and delete
                                    for j, piece in enumerate(piece_copy_right):
                                        if piece.position == [piece_copy_right[i].position[0]+1, piece_copy_right[i].position[1]+1]:
                                            target = j
                                            break

                                    # perform double jump 
                                    piece_copy_right[i].position[0] += 2
                                    piece_copy_right[i].position[1] += 2

                                    # create new board with new right move. 
                                    del piece_copy_right[target]
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
        spacer = ''
        print_row = ""
        row_size = abs(row - mid) + 2

        for space in range(int(board.size) - row_size):
            print_row += "   "
            spacer += "   "
        

        for column in range(row_size):
            if (row, column) in positions:
                print_row += ' | '
                print_row += positions[(row,column)]
                print_row += ' |'
            else:
                print_row += " | - |"
            spacer += "------"

        print(spacer)
        print(print_row)

"""helper function that runs minimax, takes player color, depth left, and if it is maxing or minimizing"""
def minimax(board, player_color, depth, ismax):
    branch_best = 0
    # The best move that will be returned to the play calling the function.
    min_best_score = 1000000
    max_best_score = -100000
    # The best case for each branch mapped to the board that the branch came from.
    evals = {}
    # The list of branches that will be evaluated. 
    branch_list = move_pieces(board, player_color)

    if depth != 0:
        for branch in branch_list:
            if player_color == 'b':
                # call minimax, next layer will be minimizing as this layer is maxing
                branch_best = minimax(branch, 'w', depth-1, not ismax)
                # print(f'branch best: {branch_best} eval: {ismax}')
                evals[branch] = branch_best

            else:
                # call minimax, next layer will be minimizing as this layer is maxing
                branch_best = minimax(branch, 'b', depth-1, not ismax)
                # print(f'branch best: {branch_best} eval: {ismax}')
                evals[branch] = branch_best
                    
        if(ismax):
            # print(f'max evals: {evals}')
            for index in evals:
                if evals[index] > max_best_score:
                    max_best_score = evals[index]
            return max_best_score
        else:
            # print(f'min evals: {evals}')
            for index in evals:
                if evals[index] < min_best_score:
                    min_best_score = evals[index]
            return min_best_score
    else:
        # print(f'root value: {board_eval(board, player_color)}')
        return board_eval(board, player_color)


"""Take in a board, the depth of search and whos turn it is right at time of analysis."""
def make_move(board, player_color, depth):
    best_score = -100000
    branch_best = 0
    # The best move that will be returned to the play calling the function.
    best_board = None
    # The best case for each branch mapped to the board that the branch came from.
    evals = {}
    # The list of branches that will be evaluated. 
    branch_list = move_pieces(board, player_color)


    for branch in branch_list:
        if player_color == 'b':
            # call minimax, next layer will be minimizing as this layer is maxing
            branch_best = minimax(branch, 'w', depth-1, 0)
            evals[branch] = branch_best

        else:
            # call minimax, next layer will be minimizing as this layer is maxing
            branch_best = minimax(branch, 'b', depth-1, 0)
            evals[branch] = branch_best

    # Find the branch with the max branch best
    for index in evals:
        if evals[index] > best_score:
            best_score = evals[index]
            best_board = index

    return best_board

"""Takes in a board and desired color and returns an interger that represents the goodness of a board relating to the given color.
    The larger the number the better the board. Score ranges from 100 = win to -100 = loss."""
def board_eval(board, color):
    # piece counts
    wcount = 0
    bcount = 0
    # number of w or b pieces in the endzone
    wend = 0
    bend = 0
    #average position of pieces. W wants this to approach (board.size*2)-4, and B wants this to approach 0
    bposition_total = 0
    wposition_total = 0

    bposition_avg = None
    wposition_avg = None

    # score tallied from how close all your pieces are to the end zone
    movescore = 0
    # score from how many pieces youhave over the enemy.
    piecescore = 0

    # count number of each type of piece
    for piece in board.pieces:
        if piece.color == 'w':
            wcount += 1
            if piece.position[0] == (board.size*2)-4:
                wend += 1
            else:
                wposition_total += piece.position[0]
        else:
            bcount+= 1
            if piece.position[0] == 0:
                bend += 1
            else:
                bposition_total += piece.position[0]


    # check win conditions relating to the number of pieces on the board.
    if bcount == 0:
        if color == 'w':
            return 100
        else:
            return -100
    elif wcount == 0:
        if color == 'b':
            return 100
        else:
            return -100

    # check win conditions relating to end goal
    if wend == wcount:
        if color == 'w':
            return 100
        else:
            return -100
    elif bend == bcount:
        if color == 'b':
            return 100
        else:
            return -100

    # Calculate move score via subtracting the percentage of your pieces in the end versus thiers, and adding how close your pieces are to the end
    if color == 'w':
        for piece in range(wend):
            movescore += (floor(100/wcount))
        for piece in range(bend):
            movescore -= (floor(100/bcount))
        wposition_avg = wposition_total/wcount
        # the closer the the end on average the pieces are the more the left side will minimize
        movescore += 20 - (abs((board.size*2)-4-wposition_avg)*2)
    else:
        for piece in range(wend):
            movescore -= (floor(100/wcount))
        for piece in range(bend):
            movescore += (floor(100/bcount))
        bposition_avg = bposition_total/bcount
        # the closer the the end on average the pieces are the more the left side will minimize
        movescore += 20 - bposition_avg*2

    # Calculate piece score based on how many pieces you have left
    if color == 'w':
        piecescore = 50*((wcount - bcount)/(wcount+bcount))
    else:
        piecescore = 50*((bcount - wcount)/(wcount+bcount))

    return int(floor(movescore+piecescore))


def deconstruct_board(board):

    num_rows = int((board.size*2)-3)
    mid = board.middle
    positions = {}

    board_array = []

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

        board_array.append(print_row)

    return board_array

"""Returns next best move given the board, the play who is moving, and the search depth."""
def oskaplayer(boardstring, player_color, depth):

    board = generate_board(boardstring)
    next_move = make_move(board, player_color, depth)

    return deconstruct_board(next_move)
    