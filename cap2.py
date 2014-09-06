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

"""
x = [3,4,6,2,5,1,0,7,9,8]
print x
inverse_sort(x)

# 2.1-3
print "\n# 2.1-3"
A = [8, 5, 9, 3, 7, 1, 4,]
v = 2

def do213():
    for i in range(0, len(A)):
        key = i
        if A[key] == v:
            return key
    return None
print do213()


# 2.2-2
print "\n# 2.2-2"
A = [8, 5, 9, 3, 7, 1, 4,]

for i in range(0, len(A) - 1):
    print A
    key = i
    for j in range(i, len(A)):
        key2 = j
        if A[key] > A[key2]:
            key = key2
    tmp = A[i]
    A[i] = A[key]
    A[key] = tmp

# 2.2-3
print "\n# 2.2-3"
A = [8, 5, 9, 3, 7, 1, 4,]
v = 2

def do223():
    for i in range(0, len(A)):
        key = i
        if A[key] == v:
            return key
    return None
print do223()

print "Worst case teta-n"
print "Best average case (1 + 2 + n)/n => n(n+1)/2n -> (n+1)/2 -> teta-n"
"""
def main():
    print("run functions")
    search_problem(10)


if __name__ == "__main__":
    main()
