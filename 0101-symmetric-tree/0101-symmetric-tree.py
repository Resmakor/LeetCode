# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self, L, R):
        if not L and not R:
            return True
        if not L or not R:
            return False
        return L.val == R.val and self.isMirror(L.left, R.right) and self.isMirror(L.right, R.left)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isMirror(root.left, root.right)

        
            