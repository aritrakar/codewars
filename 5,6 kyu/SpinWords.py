# https://www.codewars.com/kata/5264d2b162488dc400000001
# Write a function that takes in a string of one or more words, and returns the same string, but with all 
# five or more letter words reversed (like the name of this kata). Strings passed in will consist of only
# letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    words = sentence.split(" ")
    s = ""
    for word in words:
        if len(word) >= 5:
            s += word[::-1]
        else:
            s += word
        s += " "
    return s.strip()
