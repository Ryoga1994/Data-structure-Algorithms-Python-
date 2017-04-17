import strassen as s

import numpy as np

A, B = s.create_matrix('random_1_1.txt', 1000)

C = s.convention_matrix_mult(A,B)

C = s.Strassen_opt(A,B,100)

A = np.array(A)
B = np.array(B)
np.dot(A,B)

