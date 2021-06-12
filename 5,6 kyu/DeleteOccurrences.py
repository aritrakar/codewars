# https://www.codewars.com/kata/554ca54ffa7d91b236000023
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. 
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead 
# to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order,max_e):
    # code here
    d = dict()
    arr = []
    i = 0
    for o in order:
        if d.get(o) == None:
            d[o] = 1
            arr.append(o)
        else:
            d[o] += 1
            if d.get(o) <= max_e:
                arr.append(o)
    return arr
