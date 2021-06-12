# https://www.codewars.com/kata/5511b2f550906349a70004e1
  
# Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of a^b. 
# Note that a and b may be very large!

def last_digit(n1, n2):
    reference = {2: [6,2,4,8], 3: [1,3,9,7], 4: [6,4], 7: [1,7,9,3], 8:[6,8,4,2], 9:[1,9]}
    if n2 == 0:
        return 1
    l = n1 % 10
    if l in [0,1,5,6]:
        return l
    if l in [2,3,7,8]:
        d = n2 % 4
        return reference.get(l)[d]
    if l in [4,9]:
        e = n2 % 2
        return reference.get(l)[e]
