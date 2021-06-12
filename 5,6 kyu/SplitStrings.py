# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

def solution(s):
    l = len(s)
    if l % 2 == 1:
        s += '_'
        l += 1
    arr = []
    for x in range(0,l-1, 2):
        arr.append(s[x:x+2])
    return arr
