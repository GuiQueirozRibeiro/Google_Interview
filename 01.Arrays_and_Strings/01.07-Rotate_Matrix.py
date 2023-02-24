'''
01.07 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
      bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

#Time: O(n*n) Space: O(1)

def rotateMatrix(matrix): 
    n = len(matrix) 
    layer = n//2 + n%2
    for i in range(layer): 
        first = i 
        last = n - first - 1 
        for j in range(first, last): 
            walker = j - first
            
            top = matrix[first][j] 
            right = matrix[j][last] 
            botton = matrix[last][last-walker] 
            left = matrix[last-walker][first]

            matrix[first][j] = left 
            matrix[j][last] = top 
            matrix[last][last-walker] = right 
            matrix[last-walker][first] = botton 
    return matrix