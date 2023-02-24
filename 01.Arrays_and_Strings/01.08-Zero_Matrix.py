'''
01.08 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
      column are set to O.
'''

#Time: O(MxN) Space: O(1)

def zeroMatrix(matrix):
    M = len(matrix)
    N = len(matrix[0])
    line = False
    column = False
    for i in range(M):
        if matrix[i][0] == 0:
            line = True
            break 
    for j in range(N):
        if matrix[0][j] == 0:
            column = True
            break
    for i in range(1,M):
        for j in range (1,N):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0
    for i in range(1,M):
        for j in range (1,N):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    count1 = 0
    count2 = 0
    while line and count1 < M:
        matrix[count1][0] = 0
        count1 +=1
    while column and count2 < N:
        matrix[0][count2] = 0
        count2 += 1
    return matrix