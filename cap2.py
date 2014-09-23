#!/usr/bin/env python
import random

def sort():
    x = []
    i = 0
    while i < 7:
        x.append(random.randint(0,10))
        i += 1
    print x
    
    # sort-insert algorithm
    #x = [5,2,4,6,1,3]
    
    for i in range(1, len(x)):
        key = x[i]
        print "key -> ", key
        j = i - 1
        print "j -> ",j
    
        while j >= 0 and x[j] > key:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key
    
    print x
    
def inverse_sort1(A):
    """Exercises 2.1-2."""
    for j in range(1, len(A)):
        # j = 8
        key = A[j] # key = 9
        i = j - 1  # i = 6

        # A[i] = 0; A[i + 1] = 9
        while i >= 0 and A[i] < key:
            # A = [3, 4, 6, 2, 5, 1, 9, 0, 7, 8]
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A


def inverse_sort2(A):
    """
    Exercises 2.1-2.
    This is not so efficient.
    """
    for j in range(1, len(A)):
        # j = 8
        key = A[j] # key = 9
        i = j - 1  # i = 6

        # A[i] = 0; A[i + 1] = 9
        while i >= 0 and A[i] < A[i+1]:
            # A = [3, 4, 6, 2, 5, 1, 9, 0, 7, 8]
            A[i+1] = A[i]
            A[i] = key
            i = i - 1
    return A


def search_problem(v):
    """Enter value ``v`` to do a linear search in a list of ints."""
    from random import randint

    a = []
    i = 0
    while i < 100:
        a.append(randint(0, 100))
        i += 1

    for i in range(0, len(a)):
        if a[i] == v:
            print(i)
            return i
    print("None")
    return None

# 2.1-4
def do214(A, B):
    import re
    A = str(bin(A))
    A = re.sub("^0b", "", A)
    A = list(A)
    print(A)

    B = str(bin(B))
    B = re.sub("^0b", "", B)
    B = list(B)
    print(B)

    if len(A) == len(B):
        n = len(A)
        C = [0]*(n+1)

        i = n-1
        while i > 0:
            sum = int(A[i]) + int(B[i]) + int(C[i])
            print(sum)
            if sum > 1:
                C[i+1] = sum % 2
                C[i] = sum / 2
            else:
                C[i+1] = sum
            print(C)
            i -= 1
        return C
    else:
        return "Enter other numbers of the same length when in binary."


# recursive insertion sort
# ========================
def resort(lista):
    if len(lista) <= 1:
        return lista
    else:
        return insertone(lista[0], resort(lista[1:]))


def insertone(lista, element):
    print(lista)
    if len(lista) == 0:
        return [element]
    if lista[0]:
        return [element] + lista
    else:
        return insertone(element, lista[1:]) + [lista[0]]

def main():
    #print resort([3,2,1])


if __name__ == "__main__":
    main()
