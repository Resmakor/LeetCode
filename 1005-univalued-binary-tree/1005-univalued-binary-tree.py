# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left and root.right:
            if root.left.val == root.right.val and root.left.val == root.val:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            return False
        if root.left: 
            if root.left.val == root.val:
                return self.isUnivalTree(root.left)
            return False
        if root.right: 
            if root.right.val == root.val:
                return self.isUnivalTree(root.right)
            return False
        return True
        
