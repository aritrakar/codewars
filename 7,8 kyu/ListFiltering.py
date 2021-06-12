# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# Create a function that takes a list of non-negative integers and 
# strings and returns a new list with the strings filtered out.

def filter_list(l):
    return list(filter(lambda x: type(x) != str, l))
