# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:33:43 2017

@author: Ruhan
"""

import numpy as np
import math
import time

def is_power2(num):
    """check whether a number is power of 2"""

    # a number is a power of 2 only if its 8 bits representation has only one '1'
    return ((num & (num - 1)) == 0) and num != 0

def Fibonacci(n):
    """calculate Fibonacci number using matrix multiplication"""
    F_0_1 = np.array([0,1])

    multiplier = np.array([[0,1],[1,1]])

    # calculate n power of multiplier
    multi = multiplier

    if(is_power2(n)):   # if n is a power of 2

        for i in range(int(math.log(n,2))):
            multi = np.dot(multi,multi)%65536

    else:   # if n is not a power of 2
        res = n - int(math.pow(2,int(math.log(n,2)))) # rest power index

        for i in range(int(math.log(n,2))):
            multi = np.dot(multi, multi)%65536

        for i in range(res):
            multi = np.dot(multi,multiplier)%65536

    return (np.dot(multi,F_0_1)[0])

def Fibonacci_one_minute(elapse):
    """calculate Fibonacci number using matrix multiplication"""
    F_0_1 = np.array([0,1])

    multiplier = np.array([[0,1],[1,1]])
    multi = multiplier
    # stop in 60 seconds
    end_time = time.time() + elapse
    exp = 1
    num_iter = 0

    while(time.time()<end_time):

        # calculate n power of multiplier
        multi = np.dot(multi, multi) % 65536
        num_iter += 1


    return (num_iter) # F(n) should be 2^num_iter power of multiplier

n = Fibonacci_one_minute(60)

if __name__=="__main__":
    # import argparse,os
    # from time import time
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument("n", help="n to calculate Finbonacci number")
    # args = parser.parse_args()

    # calculate time need for calculate Fibonacci number of n
    # start = time()
    # Fibonacci(int(args.n))
    # stop = time()
    #
    # print("Time to calculate Fibonacci (%s) by matrix: %f s"%(args.n,stop-start))

    n = Fibonacci_one_minute(60)

    print("n retrieved by matrix in 60 seconds: 2^%d"%(n))