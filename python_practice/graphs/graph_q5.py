'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        fresh, rotten = 0, deque()
        minutes = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))
        
        while rotten and fresh:
            size = len(rotten)
            while size > 0:
                x, y = rotten.popleft()
                for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        rotten.append((nx, ny))
                        grid[nx][ny] = 2
                        fresh -= 1
                size -= 1
            minutes += 1 
        return minutes if not fresh else -1

# Time: O(M x N), each orange visited exactly once. Space: O(M x N) because of queue storing at most M x N oranges  