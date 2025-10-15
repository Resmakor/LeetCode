# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.diameter = 0
    def max_depth(self, node):
        if node is None:
                return 0
        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth(root)
        return self.diameter