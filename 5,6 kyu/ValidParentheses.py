# https://www.codewars.com/kata/52774a314c2333f0a7000688

# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

def valid_parentheses(string):
    #your code here
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        if s == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return len(stack) == 0
