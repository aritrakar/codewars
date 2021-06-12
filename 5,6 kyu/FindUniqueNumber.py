# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# There is an array with some numbers. All numbers are equal except for one. 
# Try to find it!It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    # your code here
    d = {}
    for a in arr:
        if d.get(a) == None:
            d[a] = 1
        else:
            d[a] += 1
    return list(d.keys())[(list(d.values()).index(1))]
