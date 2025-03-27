'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
'''

from collections import deque 

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.bfs(grid, x, y)
                    num_islands += 1
        return num_islands

    def bfs(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            grid[x][y] = "0"
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    queue.append((nx, ny))
       
