# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.output = []
    def inorder(self, root):
        if not root:
                return
        self.inorder(root.left)
        self.output.append(root.val)
        self.inorder(root.right)
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.inorder(root)
        return self.output