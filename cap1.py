#!/usr/bin/env python

import math
import timeit
import numpy as np


################################
print "Logarithm function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,1000, num=10):
    time = math.log(i)

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True


################################
print "\nSquare root function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,300, num=300):
    time = math.sqrt(i)

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True


################################
print "\nn function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,20, num=1000):
    time = i

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True


################################
print "\nn log n function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,16, num=1000):
    time = i*math.log(i)

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True


################################
print "\nn2 function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,8, num=100000):
    time = i*i

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True


################################
print "\nn3 function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.logspace(1,6, num=100000):
    time = i*i*i

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True


################################
print "\n2.pow(n) function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.arange(100):
    time = math.pow(2,i)

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True



################################
print "\nFactorail function"

second = False
minute = False
hour = False
day = False
month = False
year = False
century = False
time = 0
for i in np.arange(100):
    time = math.factorial(i)

    if second == False:
        if time/1000000 > 1.0:
            print "# 1 second, n =", i
            second = True
    if minute == False:
        if time/(1000000*60) > 1.0:
            print "# 1 minute, n =", i
            minute = True
    if hour == False:
        if time/(1000000*60*60) > 1.0:
            print "# 1 hour, n =", i
            hour = True
    if day == False:
        if time/(1000000*60*60*24) > 1.0:
            print "# 1 day, n =", i
            day = True
    if month == False:
        if time/(1000000*60*60*24*30) > 1.0:
            print "# 1 month, n =", i
            month = True
    if year == False:
        if time/(1000000*60*60*24*30*365) > 1.0:
            print "# 1 year, n =", i
            year = True
    if century == False:
        if time/(1000000*60*60*24*30*365*100) > 1.0:
            print "# 1 century, n =", i
            century = True
