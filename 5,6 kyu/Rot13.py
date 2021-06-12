# https://www.codewars.com/kata/530e15517bc88ac656000716
#
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters 
# after it in the alphabet. ROT13 is an example of the Caesar cipher. Create a function that takes
# a string and returns the string ciphered with Rot13. If there are numbers or special characters
# included in the string, they should be returned as they are. Only letters from the latin/english 
# alphabet should be shifted, like in the original Rot13 "implementation". Please note that using 
# "encode" is considered cheating.

def rot13(message):
    res = ""
    temp = ""
    for c in message:
        if str.isalpha(c):
            if str.islower(c):
                # lower case
                if ord(c) + 13 > ord("z"):
                    temp = chr(ord("a") + (ord(c) + 13) - ord("z") - 1)
                else:
                    temp = chr(ord(c) + 13)
            else:
                # upper case
                if ord(c) + 13 > ord("Z"):
                    temp = chr(ord("A") + (ord(c) + 13) - ord("Z") - 1)
                else:
                    temp = chr(ord(c) + 13)
            res += temp
        else:
            res += c
    print(res)
    return res
