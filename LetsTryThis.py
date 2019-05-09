#! /usr/bin/env python3
#Lucas Marchesani

from math import *
from time import *


def calcPi():
    try:
        # import version included with old SymPy
        from sympy.mpmath import mp
    except ImportError:
        # import newer version
        from mpmath import mp
    mp.dps = 3000000  # set number of digits
    return (mp.pi)


def main():
    inserted = "!!!!!!!!!"
    date = input("Input your birthday (mmddyy)\n")
    print("In the text file that is created, the date will be prefaced by a bunch of exclamation marks")
    start_time = clock()
    fp = open ("piDay.txt", "w+")
    pi_digits = calcPi()
    index_of = str(pi_digits).find(date)
    if (index_of==-1):
        print("not found")
    else:
        print("Your number is found at the index number", index_of)
        new_pi = str(pi_digits)[:index_of] + inserted + str(pi_digits)[index_of:]
        fp.write(str(new_pi))
    #this is where the code for finding the date will be
    print (clock() - start_time, "seconds")
    fp.close()
main()