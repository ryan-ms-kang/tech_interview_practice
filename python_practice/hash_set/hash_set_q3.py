'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Optimized; Time complexity: O(N^2)
        row_count = {}
        for row in grid:
            row_tupled = tuple(row)
            if row_tupled not in row_count:
                row_count[row_tupled] = 0
            row_count[row_tupled] += 1

        col_count = {}
        for y in range(len(grid[0])):
            curr_col = []
            for x in range(len(grid)):
                curr_col.append(grid[x][y])
            col_tupled = tuple(curr_col)
            if col_tupled not in col_count:
                col_count[col_tupled] = 0
            col_count[col_tupled] += 1

        pairs = 0
        for row in row_count:
            if row in col_count:
                pairs += (col_count.get(row) * row_count.get(row))
        return pairs

        '''
        # Brute Force; Time complexity: O(N^2) where N = number of elements in one row
        
        cols = []
        pairs = 0
        for y in range(len(grid[0])):
            col = []
            for x in range(len(grid)):
                col.append(grid[x][y])
            cols.append(col)

        for row in grid:
            for col in cols:
                if row == col:
                    pairs += 1
        return pairs
        '''
