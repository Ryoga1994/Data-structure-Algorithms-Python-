# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:31:55 2017

@author: Ruhan
"""
import time
import math

def Fibonacci(n):
    """recursively calculate Fibonacci number"""
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci_mod(n):
    """recursively calculate Fibonacci number and return number modulo 65536"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (Fibonacci(n - 1)%65536 + Fibonacci(n - 2)%65536)% 65536

# Fibonacci(10)

# largest Fibonacci number computed in one minute of machine time

# the unit of machine time could be us

if __name__=="__main__":
    import argparse,os
    from time import time

    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="n to calculate Finbonacci number")
    args = parser.parse_args()

    # calculate time need for calculate Fibonacci number of n
    start = time()
    Fibonacci_mod(int(args.n))
    stop = time()

    print("Time to recursively calculate Fibonacci(%s): %f s"%(args.n,stop-start))


