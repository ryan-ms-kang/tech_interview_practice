'''
You're given an m x n grid, where:

'W' represents a wall

'E' represents an enemy

'0' represents an empty cell

You can place one bomb in an empty cell ('0'). The bomb kills all enemies in the same row and column until it hits a wall ('W').

Return the maximum number of enemies you can kill with one bomb.
'''

class Solution(object):
    def bomb(self, grid):
        max_killed = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0":
                    max_killed = max(max_killed, self.dfs(grid, x, y))
        return max_killed
    
    def dfs(self, grid, x, y):
        kill_count = 0
        
        # Top
        for x2 in range(x - 1, -1, -1):
            if grid[x2][y] == "E":
                kill_count += 1
            elif grid[x2][y] == "W":
                break
        
        # Bottom
        for x2 in range(x + 1, len(grid)):
            if grid[x2][y] == "E":
                kill_count += 1
            elif grid[x2][y] == "W":
                break
        
        # Left
        for y2 in range(y - 1, -1, -1):
            if grid[x][y2] == "E":
                kill_count += 1
            elif grid[x][y2] == "W":
                break

        # Right
        for y2 in range(y + 1, len(grid[0])):
            if grid[x][y2] == "E":
                kill_count += 1
            elif grid[x][y2] == "W":
                break
    
        return kill_count

# Worst case is for each cell, check entire row and col -> O(m + n) * O(mn)

grid = [
    ['0', 'E', 'W', 'E'],
    ['E', '0', 'W', 'E'],
    ['E', 'E', '0', '0'],
    ['W', 'E', 'E', 'E']
]

test = Solution()
print(test.bomb(grid)) 
                    
                    