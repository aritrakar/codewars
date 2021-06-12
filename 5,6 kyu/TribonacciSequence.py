# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    #your code here
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        return signature[:2]
    store = signature
    for x in range(3,n):
        store.append(store[x - 3] + store[x - 2] + store[x - 1])
    return store
