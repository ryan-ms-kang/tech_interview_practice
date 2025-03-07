'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find the in-order successor, copy its value, and delete the successor
                root.val = self.getMin(root.right).val
                root.right = self.deleteNode(root.right, root.val)
        return root 

    def getMin(self, root):
        # Traverse left to find the smallest node in the right subtree
        while root.left:
            root = root.left
        return root

# O(h), where h is the height of the tree. Worst case O(N) where N = num of nodes, in the case an unbalanced tree