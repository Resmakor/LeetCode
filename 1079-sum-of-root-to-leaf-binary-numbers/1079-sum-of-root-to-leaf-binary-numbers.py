# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def recursion(root, result):
            if not root:
                return 0
            result = result * 2 + root.val
            if not root.left and not root.right:
                return result
            return recursion(root.left, result) + recursion(root.right, result)
        return recursion(root, 0)
