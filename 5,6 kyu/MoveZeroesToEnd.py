# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    l = len(array)
    zeros = 0
    arr = []
    for a in array:
        if a == 0:
            zeros += 1
        else:
            arr.append(a)
    for y in range(zeros):
        arr.append(0)
    return arr
