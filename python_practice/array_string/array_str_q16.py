"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        boxes, rows, cols = defaultdict(set), defaultdict(set), defaultdict(set)

        for x in range(len(board)):
            for y in range(len(board[0])):
                curr_cell = board[x][y]
                if curr_cell != ".":
                    box_index = (x // 3, y // 3)

                    if curr_cell in boxes[box_index]:
                        return False
                    boxes[box_index].add(curr_cell)

                    if curr_cell in rows[x]:
                        return False
                    rows[x].add(curr_cell)

                    if curr_cell in cols[y]:
                        return False
                    cols[y].add(curr_cell)
        return True

