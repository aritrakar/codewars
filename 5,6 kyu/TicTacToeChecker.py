# https://www.codewars.com/kata/525caa5c1bf619d28c000335
  
# Our goal is to create a function that will check that for us
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O".
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    winner = ''
    openSpots = 0

    for i in range(0,3): #Horizontal
        if (board [i][0] == board[i][1] == board[i][2] != 0):
            winner = board[i][0]
            break

    for i in range(0,3): #Vertical
        if (board [0][i] == board[1][i] == board[2][i] != 0):
            winner = board[0][i]
            break

    #Diagonals:
    if (board[0][0] == board[1][1] == board[2][2] != 0):
        winner = board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0] != 0):
        winner = board[0][2]
        
    #Open spots
    for i in range(0,3):
        for j in range(0,3):
            if (board[i][j] == 0):
                openSpots += 1

    if (winner == ''):
        if openSpots == 0:
            return 0
        else:
            return -1
    else:
        return int(winner)
