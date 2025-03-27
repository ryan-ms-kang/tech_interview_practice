'''
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
'''

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  
        shortest = float("inf")

        while queue:
            x, y, step = queue.popleft()
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x != entrance[0] or y != entrance[1]):
                shortest = min(shortest, step)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == ".":
                    queue.append((nx, ny, step + 1))
                    maze[nx][ny] = "+"
        return shortest if shortest != float("inf") else -1