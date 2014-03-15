#!/usr/bin/env python
import random

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
