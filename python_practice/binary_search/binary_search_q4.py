'''
You are given a binary matrix mat where:

Each row is sorted in non-decreasing order (0s may appear before 1s).
Your task is to find the leftmost column (smallest index) that contains at least one 1.
If there are no 1s in the matrix, return -1.

E.g.) 

matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

return 0
'''

def leftMost(matrix):
    if not matrix:
        return -1
    
    # for col in range(len(matrix[0])):
    #     for row in range(len(matrix)):
    #         if matrix[row][col] == 1:
    #             return col
    # return -1
    
    leftmost_index = float("inf")

    for row in matrix:
        curr_min_index = float("inf")
        low, high = 0, len(row) - 1

        while low <= high:
            mid = (low + high) // 2
            if row[mid] == 1:
                curr_min_index = mid
                high = mid - 1
            else:
                low = mid + 1

        leftmost_index = min(leftmost_index, curr_min_index)
    
    return leftmost_index if leftmost_index != float("inf") else -1
    

