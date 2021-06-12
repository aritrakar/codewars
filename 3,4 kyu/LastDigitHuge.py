# https://www.codewars.com/kata/5518a860a73e708c0a000027
  
# For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

def last_digit(lst):
    if len(lst) == 0:
        return 1
    res = 1
    for x in lst[::-1]:
        res = x ** (res if res < 4 else res % 4 + 4)
    return res % 10
