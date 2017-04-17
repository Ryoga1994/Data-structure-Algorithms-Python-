# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:33:55 2017

@author: Ruhan
"""
import time


def Fibonacci(n):
    """iteratively calculate Fibonacci number"""

    # initialize array
    A_0 = 0
    A_1 = 1

    for i in range(2,n+1):
        A = (A_0%65536 + A_1%65536) % 65536
        A_0 = A_1
        A_1 = A

    return (A)

def Fibonacci_one_min(elapse_time):
    """iteratively calculate Fibonacci number"""

    A_0 = 0
    A_1 = 1
    index = 1

    end_time = time.time()+elapse_time

    while(time.time()<end_time):

        A = (A_0%65536 + A_1%65536) % 65536
        index += 1 # record n
        A_0 = A_1
        A_1 = A

    return (index)



if __name__=="__main__":
    import argparse,os
    import time

    import math
    # parser = argparse.ArgumentParser()
    # parser.add_argument("n", help="n to calculate Finbonacci number")
    # args = parser.parse_args()
    #
    # # calculate time need for calculate Fibonacci number of n
    # start = time()
    # Fibonacci(int(args.n))
    # stop = time()
    #
    # print("Time to interactively calculate Fibonacci(%s): %f s"%(args.n,stop-start))

    n = Fibonacci_one_min(60)

    print("n retrieved by iterative in 60 seconds: %d"%(n))

