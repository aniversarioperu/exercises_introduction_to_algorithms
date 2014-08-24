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
    
def inverse_sort(x):    
    for i in range(1, len(x)):
        key = x[i]
        print key
        j = i - 1

        while j >= 0 and x[j] < key:
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = key
    print x

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
