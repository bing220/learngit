import laguide as lag
import numpy as np

# Input your matrix here
A=np.array([[1,3,4,7], [3,9,7,1]])

print("The original matrix is:\n")
print(A)
print("\n")

A_reduced = lag.FullRowReduction(A)
print("The reduced row echelon matrix is:\n")
print(A_reduced)


