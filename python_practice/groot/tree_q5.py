'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, path_max):
            if not root:
                return 0
            elif root.val >= path_max:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            else: 
                return helper(root.left, path_max) + helper(root.right, path_max)
        return helper(root, root.val)
            
# O(N), where N = num of nodes in the tree. We visit each node exactly once