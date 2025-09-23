# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.leaves = []
    def getLeaves(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.leaves.append(root.val)
            return
        self.getLeaves(root.left)
        self.getLeaves(root.right)
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        self.getLeaves(root1)
        leaves1 = self.leaves
        self.leaves = []
        self.getLeaves(root2)
        return leaves1 == self.leaves
        