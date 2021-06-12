# https://www.codewars.com/kata/54e6533c92449cc251001667
# Implement the function unique_in_order which takes as argument a sequence and returns a 
# list of items without any elements with the same value next to each other and preserving 
# the original order of elements.

def unique_in_order(iterable):
    if len(iterable) == 1:
        return [iterable]
    store = []
    l = len(iterable)
    for i in range(l - 1):
        if iterable[i] != iterable[i+1]:
            store.append(iterable[i])
        if i == l - 2:
            store.append(iterable[i+1])
    return store
