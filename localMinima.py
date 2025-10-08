import numpy as np

matrix =np.array([
[9,8,7,6,5],
[5,3,4,7,8],
[6,7,2,8,9],
[8,6,5,4,3],
[9,7,6,5,4]])

rows, cols = matrix.shape

for i in range(1,rows-1):
    for j in range(1,cols-1):
       if matrix[i-1][j]>matrix[i][j] and matrix [i+1][j]>matrix[i][j] and matrix [i][j-1]>matrix[i][j] and matrix [i][j+1]> matrix [i][j]:
        print ("local minima is at",(i,j),"with value", matrix[i][j])