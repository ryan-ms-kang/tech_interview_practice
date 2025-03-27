'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if self.dfs(board, x, y, word, 0):
                        return True
        return False
    
    def dfs(self, board, x, y, word, i):
        if i == len(word):
            return True
        if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or board[x][y] != word[i]:
            return False

        backtrack = board[x][y]
        board[x][y] = "#"
        
        left = self.dfs(board, x - 1, y, word, i + 1)
        right = self.dfs(board, x + 1, y, word, i + 1)
        top = self.dfs(board, x, y + 1, word, i + 1)
        bottom = self.dfs(board, x, y - 1, word, i + 1)

        board[x][y] = backtrack
        return top or bottom or left or right
        
         
# O(M x N)