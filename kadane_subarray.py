# find index i,j for 1-d array A that has max sum for subarray A[i:j]

def max_sub_index(A):
    """find index i,j for 1-dimension array A that has max sum for subarray A[i:j]"""

    max_ending_here = max_so_far = A[0]

    i_meh = j_meh = 0
    i_msf = j_msf = 0

    for k in range(1,len(A)):

        # if previous elements adds to negative, we throw them away
        if max_ending_here < 0:
            # i indicate start index of max subarray ending here
            i_meh = k
            j_meh = k
        # if previous elements adds to positive
        else: # if max_ending_here > 0
            j_meh = k

        max_ending_here = max(A[k], max_ending_here + A[k])

        # if max subarray ending here is larger than previous record
        if max_so_far < max_ending_here:
            # j indicate the end index of max subarray current hold
            i_msf = i_meh
            j_msf = j_meh

        max_so_far = max(max_so_far, max_ending_here)

    return i_msf,j_msf

def main():

    A = [3,2,1,-8,-5]

    import random
    random.seed(111)

    A = [3,7,8,8,6,4,-1,-10,9,-7,9,9,-100,1000]
    max_sub_index(A)

    A[max_sub_index(A)[0]:max_sub_index(A)[1]+1]
