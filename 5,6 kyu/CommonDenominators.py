# https://www.codewars.com/kata/54d7660d2daf68c619000d95

from functools import reduce

def gcd(a,b):
    while (b):
        a, b = b, a % b
    return a
  
def lcm_multiple(lst):
    return reduce(lambda x, y : int(x*y/gcd(x,y)), lst)

def convert_fracts(lst):
    if len(lst) < 2:
        return lst
    lcm = lcm_multiple([ y for x, y in lst])
    return [ [int(x*lcm)//y, lcm] for x, y in lst]
