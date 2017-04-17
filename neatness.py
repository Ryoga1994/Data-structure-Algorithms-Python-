# assignment 3, problem 6

# input raw text, maximum line length M
# output text split into lines appropriately, and the numeric value of penalty
raw_text = "I am a good boy."

import math

def penalty(words_lis,i,j,M):
    """return penalty when put word i,...,j on the same line"""
    s = M - j + i - sum([len(ele) for ele in words_lis[(i-1):j]])
    if s<0:
        return float('inf')
    elif j == len(words_lis) and s>=0:
        return 0
    else:
        return s**3


def neatness(raw_text,M):
    """output neatness print style for given text"""
    import numpy as np

    words_lis = raw_text.split()
    Cost = [0]*(len(words_lis)+1)
    split = [0]*(len(words_lis)+1)

    # calculate penalty matrix
    penals = np.zeros((len(words_lis)+1,len(words_lis)+1))

    for i in range(1,len(words_lis)+1):
        penals[i][i] = penalty(words_lis,i,i,M)
        for j in range(i+1,len(words_lis)+1):
            penals[i][j] = penalty(words_lis,i,j,M)

    # calculate Cost

    for j in range(1,len(words_lis)+1):
        Cost[j] = float('inf')
        for i in range(1,j+1):
            if Cost[i-1]+penals[i][j] < Cost[j]:
                Cost[j] = Cost[i-1] + penals[i][j]
                split[j] = i

    s = split[len(words_lis)]
    e = len(words_lis)

    while True:
        t = ''
        for i in range(s-1,e):
            t = t + ' ' + words_lis[i]
        print(t)
        e = s - 1
        if s == split[s]:
            s = s -1
        else:
            s = split[s]

        if s <= 2:
            break

    return Cost[-1]


def main():
    con = open("BuffyReview.txt",'r')
    raw_text = con.readline().strip('\n')

    min_p1 = neatness(raw_text,40)
    print(min_p1)

    min_p2 = neatness(raw_text, 72)
    print(min_p2)

main()