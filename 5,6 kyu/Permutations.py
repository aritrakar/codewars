# https://www.codewars.com/kata/5254ca2719453dcc0b00027d

# In this kata you have to create all permutations of an input string and remove duplicates, if present. 
# This means, you have to shuffle all letters from the input in all possible orders.

from itertools import permutations as p

def permutations(string):    
    perms = list(p(list(string)))
    res = list(map(lambda x: "".join(x), perms))
    return set(res)
