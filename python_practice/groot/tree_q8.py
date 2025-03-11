'''
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
    
        def traverse(root, go_left, curr_path):
            if not root:
                return curr_path - 1 
            if go_left:
                l = traverse(root.left, False, curr_path + 1)
                r = traverse(root.right, True, 1)
            else:
                r = traverse(root.right, True, curr_path + 1)
                l = traverse(root.left, False, 1)
            return max(l, r)

        return max(traverse(root.left, False, 1), traverse(root.right, True, 1))
    
    # Time: O(N) where N = num of nodes in the tree; Space: O(h) where h = height of tree