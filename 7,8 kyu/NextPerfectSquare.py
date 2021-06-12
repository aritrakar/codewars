# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train
# Complete the findNextSquare method that finds the next integral perfect square after the one 
# passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) 
# is also an integer. If the parameter is itself not a perfect square then -1 should be returned. 
# You may assume the parameter is non-negative.

import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    rt = int(math.sqrt(sq))
    if sq == rt * rt:
        return (rt + 1) * (rt + 1)
    return -1
