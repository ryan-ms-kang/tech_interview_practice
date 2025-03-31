'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for x in range(len(matrix) // 2):
            # n - x since we're replacing n - 1 cells
            for y in range(x, n - x):
                tl = (x, y)
                tr = (y, n - x)
                br = (n - x, n - y)
                bl = (n - y, x)
                
                tl_copy = matrix[tl[0]][tl[1]]
                tr_copy = matrix[tr[0]][tr[1]]
                br_copy = matrix[br[0]][br[1]]
                bl_copy = matrix[bl[0]][bl[1]]
    
                matrix[tl[0]][tl[1]] = bl_copy
                matrix[tr[0]][tr[1]] = tl_copy
                matrix[br[0]][br[1]] = tr_copy
                matrix[bl[0]][bl[1]] = br_copy
                
    # O(N^2) Time