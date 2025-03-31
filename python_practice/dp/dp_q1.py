'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n] * m

        dp[0][0] = grid[0][0]

        for y in range(1, n):
            dp[0][y] = dp[0][y - 1] + grid[0][y]
        
        for x in range(1, m):
            dp[x][0] = dp[x - 1][0] + grid[x][0]

        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = grid[x][y] + min(dp[x - 1][y], dp[x][y - 1])
        
        return dp[m - 1][n - 1]
    
    # Time: O(m * n)

        
        # def dfs(x, y):
        #     if not (0 <= y < len(grid[0])) or not (0 <= x < len(grid)):
        #         return float("inf")
        #     if x == len(grid) - 1 and y == len(grid[0]) - 1:
        #         return grid[x][y]
            
        #     bot = grid[x][y] + dfs(x + 1, y) 
        #     right = grid[x][y] + dfs(x, y + 1) 
        #     return min(bot, right)

        # return dfs(0, 0)
    
    # Time: O(2^(m+n)); at each cell, you have only 2 options (right, bottom) to travel; 
    # to get to bottom-right corner, you travel at most m + n times
    # so for all m + n cells you get O(2^(m + n))

        