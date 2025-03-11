'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        level = 1
        smallest_level, max_sum = float("inf"), -float("inf")    
        queue = deque([(level, root)])

        while queue:
            size = len(queue)
            curr_level_sum = 0
            while size > 0:
                curr_level, curr_node = queue.popleft()
                curr_level_sum += curr_node.val
                size -= 1
                
                for child in [curr_node.left, curr_node.right]:
                    if child:
                        queue.append((curr_level + 1, child))
 
            if max_sum < curr_level_sum or (max_sum == curr_level_sum and smallest_level > curr_level):
                smallest_level = curr_level
                max_sum = curr_level_sum

        return smallest_level
        
        
# Time: O(N), where N = num of nodes in the tree. Space: O(N), due to storing N nodes in a queue