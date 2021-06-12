# https://www.codewars.com/kata/55908aad6620c066bc00002a
# Check to see if a string has the same amount of 'x's and 'o's. The method must
# return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    x = 0
    o = 0
    for l in s:
        if 'x' == l.lower():
            x += 1
        if 'o' == l.lower():
            o += 1
    return x == o
