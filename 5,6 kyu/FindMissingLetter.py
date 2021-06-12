# https://www.codewars.com/kata/5839edaa6754d6fec10000a2
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

def find_missing_letter(chars):
    #lower = chars[0] == chars[0].lower()
    for c in range(0,len(chars)-1):
        if ord(chars[c + 1]) - ord(chars[c]) != 1:
            return chr(ord(chars[c]) + 1)
    return
