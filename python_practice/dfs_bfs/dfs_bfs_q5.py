'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n.
 You are also given an integer startValue representing the value of the start node s, 
 and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string 
consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        common_prefix = self.lca(root, startValue, destValue)
        path_to_start = self.get_path(common_prefix, startValue, "") 
        path_to_dest = self.get_path(common_prefix, destValue, "")

        return 'U' * len(path_to_start) + path_to_dest

    def lca(self, root, p, q):
        if not root:
            return None
        if root.val == p or root.val == q:
            return root

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right

    def get_path(self, root, dest, path):
        if not root:
            return 
        if root.val == dest:
            return path

        left = self.get_path(root.left, dest, path + 'L')
        right = self.get_path(root.right, dest, path + 'R')
        return left if left else right 