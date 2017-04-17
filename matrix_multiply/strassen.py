

def create_matrix(inputfile,d):
    """return matrix A, B by reading from input file"""

    # initialize matrix A, B
    A = []
    B = []
    for i in range(d):
        A.append([])
        B.append([])

    with open(inputfile,'r') as f:
        for i in range(d):
            for j in range(d):
                A[i].append(int(f.readline().strip("\n")))

        for i in range(d):
            for j in range(d):
                B[i].append(int(f.readline().strip("\n")))

    return A,B

def create_matrix_float(inputfile,d):
    """return matrix A, B by reading from input file with float number"""

    # initialize matrix A, B
    A = []
    B = []
    for i in range(d):
        A.append([])
        B.append([])

    with open(inputfile,'r') as f:
        for i in range(d):
            for j in range(d):
                A[i].append(float(f.readline().strip("\n")))

        for i in range(d):
            for j in range(d):
                B[i].append(float(f.readline().strip("\n")))

    return A,B

def convention_matrix_mult(A,B):
    """with given matrix A, B and dimension, return A*B - o(n^3)"""
    # initialize c
    d = len(A)
    C = [[0] * d for c in range(d)]

    for i in range(d):
        for j in range(d):
            # calculate entry i,j
            for k in range(d):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]

    return C

def Strassen_2n(A,B):
    """Strassen multiplication for d = 2^n"""
    d = len(A)
    if d == 1:
        return [[A[0][0]*B[0][0]]]
    padded = False

    # if dimension is odd, add zero to botton rows and right-most columns
    if not isEven(d):
        padding(A)
        padding(B)
        padded = True
        d = d + 1

    sub_d = d//2
    # split array
    a11 = [ele[:sub_d] for ele in A[:sub_d]]
    a12 = [ele[sub_d:] for ele in A[:sub_d]]

    a21 = [ele[:sub_d] for ele in A[sub_d:]]
    a22 = [ele[sub_d:] for ele in A[sub_d:]]

    b11 = [ele[:sub_d] for ele in B[:sub_d]]
    b12 = [ele[sub_d:] for ele in B[:sub_d]]

    b21 = [ele[:sub_d] for ele in B[sub_d:]]
    b22 = [ele[sub_d:] for ele in B[sub_d:]]

    # defines new matrics : 7 multiplications

    m1 = Strassen_2n(matrix_plus(a11,a22),matrix_plus(b11,b22))
    m2 = Strassen_2n(matrix_plus(a21,a22),b11)
    m3 = Strassen_2n(a11,matrix_minus(b12,b22))
    m4 = Strassen_2n(a22,matrix_minus(b21,b11))
    m5 = Strassen_2n(matrix_plus(a11,a12),b22)
    m6 = Strassen_2n(matrix_minus(a21,a11),matrix_plus(b11,b12))
    m7 = Strassen_2n(matrix_minus(a12,a22),matrix_plus(b21,b22))

    # return sub C
    c11 = matrix_plus(matrix_minus(matrix_plus(m1,m4),m5),m7)
    c12 = matrix_plus(m3,m5)
    c21 = matrix_plus(m2,m4)
    c22 = matrix_plus(matrix_plus(matrix_minus(m1,m2),m3),m6)

    ## merge sub C
    C = merge_array(c11,c12,c21,c22)

    if padded:
        strip(A)
        strip(B)
        strip(C)
    return C

def padding(A):
    """add zeros to botton rows and right-most columns"""
    # O(d)
    d = len(A)
    for i in range(d):
        A[i].append(0)
    A.append([0]*(d+1))

def strip(A):
    """remove bottom rows and right-most columns"""
    d = len(A)
    for i in range(d-1):
        del A[i][d-1]

    del A[d-1]

def isEven(_integer):
    """return true if given integer is even"""
    return _integer % 2 == 0

def matrix_plus(A,B):
    """return multiplication of matrix"""
    # initialize C
    d = len(A)

    C = [[0]*d for c in range(d)]

    for i in range(d):
        for j in range(d):
            C[i][j] = A[i][j] + B[i][j]

    return C

def matrix_minus(A,B):
    """return difference of matrix A-B"""
    # initialize C
    d = len(A)

    C = [[0] * d for c in range(d)]

    for i in range(d):
        for j in range(d):
            C[i][j] = A[i][j] - B[i][j]

    return C

def merge_array(a11,a12,a21,a22):
    """merge 4 subarray and return as list[list]"""
    s_d = len(a11)
    d = s_d * 2

    # initialize C
    C = [[0] * d for c in range(d)]

    for i in range(s_d):
        C[i][:s_d] = a11[i]
        C[i][s_d:] = a12[i]
        C[d-i-1][:s_d] = a21[s_d-i-1]
        C[d-i-1][s_d:] = a22[s_d-i-1]

    return C

def Strassen_opt(A,B,n0):
    """Strassen multiplication for d = 2^n"""
    d = len(A)
    if d <= n0:
        return convention_matrix_mult(A,B)

    padded = False

    # if dimension is odd, add zero to botton rows and right-most columns
    if not isEven(d):
        padding(A)
        padding(B)
        padded = True
        d = d + 1

    sub_d = d//2
    # split array
    a11 = [ele[:sub_d] for ele in A[:sub_d]]
    a12 = [ele[sub_d:] for ele in A[:sub_d]]

    a21 = [ele[:sub_d] for ele in A[sub_d:]]
    a22 = [ele[sub_d:] for ele in A[sub_d:]]

    b11 = [ele[:sub_d] for ele in B[:sub_d]]
    b12 = [ele[sub_d:] for ele in B[:sub_d]]

    b21 = [ele[:sub_d] for ele in B[sub_d:]]
    b22 = [ele[sub_d:] for ele in B[sub_d:]]

    # defines new matrics : 7 multiplications

    m1 = Strassen_opt(matrix_plus(a11,a22),matrix_plus(b11,b22),n0)
    m2 = Strassen_opt(matrix_plus(a21,a22),b11,n0)
    m3 = Strassen_opt(a11,matrix_minus(b12,b22),n0)
    m4 = Strassen_opt(a22,matrix_minus(b21,b11),n0)
    m5 = Strassen_opt(matrix_plus(a11,a12),b22,n0)
    m6 = Strassen_opt(matrix_minus(a21,a11),matrix_plus(b11,b12),n0)
    m7 = Strassen_opt(matrix_minus(a12,a22),matrix_plus(b21,b22),n0)

    # return sub C
    c11 = matrix_plus(matrix_minus(matrix_plus(m1,m4),m5),m7)
    c12 = matrix_plus(m3,m5)
    c21 = matrix_plus(m2,m4)
    c22 = matrix_plus(matrix_plus(matrix_minus(m1,m2),m3),m6)

    ## merge sub C
    # initialize C
    C = merge_array(c11,c12,c21,c22)

    if padded:
        strip(A)
        strip(B)
        strip(C)
    return C

def create_file(filename,d,flag):
    """create txt file for input reading matrix"""
    import random
    with open(filename,'w') as f:
        for i in range(2*d**2):
            if flag == 1:
                f.write("%d\n"%random.randint(0,1))
            elif flag == 2:
                f.write("%d\n" % random.randint(0, 2))
            elif flag == 3:
                f.write("%d\n" % random.randint(-1, 1))
            elif flag == 4:
                f.write("%f\n" % random.uniform(0,1))

def diagonal(A):
    """print diagonal entries one per line"""
    d = len(A)
    for i in range(d):
        print(A[i][i])
    print('\n') # trailing new line


def main():
    # with open('matrix.txt','w') as f:
    #     for i in range(2*d**2):
    #         f.write("%d\n"%i)

    # read file and create two matrix

    # create input file
    create_file('random_0_1.txt', 1000, 1)
    create_file('random_0_2.txt', 1000, 2)
    create_file('random_1_1.txt', 1000, 3)
    create_file('random_uni_0_1.txt', 1000, 4)

    d = 6
    A, B = create_matrix('random_1_1.txt', 6)
    A, B = create_matrix_float('random_uni_0_1.txt',10)

    C = convention_matrix_mult(A, B)

    Strassen_2n(A,B)

    Strassen_opt(A,B,6)

    # run for specific dimension
    import time
    import pandas as pd

    res = pd.DataFrame(columns=['n0','inputfile','dimension','time/s'])

    dimensions = 1000
    inputfile = "random_uni_0_1.txt"

    for dimension in dimensions:
        for n0 in range(1,dimension+1):
            A, B = create_matrix_float(inputfile, dimension)

            start_time = time.time()
            C = Strassen_opt(A, B, n0)

            res.loc[len(res)] = [n0,inputfile,dimension,time.time() - start_time]

            print("---Dimension %d ,n0 %d: %s seconds ---" % (dimension,n0,time.time() - start_time))

    # test single solutions
    import pandas as pd
    import time

    dimensions = 256
    inputfile = "random_0_1.txt"
    res = pd.DataFrame(columns=['method', 'inputfile', 'dimension', 'time/s'])

    for dimension in range(1,401):
        A, B = create_matrix(inputfile, dimension)

        start_time = time.time()
        C = Strassen_2n(A,B)

        res.loc[len(res)] = ["strassen", inputfile, dimension, time.time() - start_time]

        print("---Dimension %d : %s seconds ---" % (dimension, time.time() - start_time))

    res.to_csv('strassen.csv')



if __name__ == "__main__":
    import sys
    import time

    flag = int(sys.argv[1])
    dimension = int(sys.argv[2])
    inputfile = sys.argv[3]
    # n0 = int(sys.argv[4])

    if flag == 0:
        A,B = create_matrix(inputfile,dimension)
    elif flag == 1:
        A,B = create_matrix_float(inputfile,dimension)

    # calculate time
    # start_time = time.time()
    C = Strassen_opt(A,B,32)
    # end_time = time.time()

    diagonal(C)

    # print("--- %s seconds ---" % (time.time() - start_time))

































