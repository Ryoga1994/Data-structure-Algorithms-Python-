import numpy as np

A = "2 4 6 7 6 3 3 3 4 3 4 4 4 3 3 1"
A = [int(ele) for ele in A.split()]
n = len(A)
k = 4

def imbalance(A,n,k):
    """return the partition with minimal imbalance given A,n and k"""

    # create k + 1 array s[1], s[2],..., s[n]
    # s[k][i,j] indicate current minimum imbalance for kth part as A[i,j]
    s = {}
    partition = [0]*k

    for i in range(1,k+2):
        s[i] = np.zeros((n,n))
        s[i][:] = np.inf

    ave = sum(A)/(k+1)


    # initialize imbalance for the first part
    for j1 in range(len(A)):
        s[1][0,j1] = abs(sum(A[0:j1]) - ave)

    for p in range(2,k+2): # each part
        for i in range(1,len(A)):
            for j in range(i,len(A)):

                s[p][i,j] = max([min(s[p-1][:,i-1]),abs(sum(A[i:(j+1)])/(k+1)-ave)])

                #

    # find partition point (possible result)

    split_p = n # split should be the start of each part except the first one

    for p in range(k+1,1,-1):

        split_p = [i for i,ele in enumerate(s[p][:, (split_p-1)])
                   if ele == min(s[p][:, (split_p-1)])][0]

        partition[p-2] = split_p

    return partition

    # the minimum imbalance should be min(s[k+1][:,n])
    # return min(s[k+1][:,n-1])

imbalance(A,len(A),3)
