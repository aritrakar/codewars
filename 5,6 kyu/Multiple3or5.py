# https://www.codewars.com/kata/514b92a657cdc65150000006
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

def sss(number, base):
    if (number % base == 0):
        number -= base
    b = number - number % base
    b_n = b // base
    b_sum = b_n * (base + b) / 2
    return b_sum

def solution(number):
    if number  < 0:
        return 0
    three = sss(number, 3)
    five = sss(number, 5)
    fifteen = sss(number, 15)
    print(three, five, fifteen)
    return int(three + five - fifteen)
