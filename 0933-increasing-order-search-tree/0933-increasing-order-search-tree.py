# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.curr.right = TreeNode(node.val)
            self.curr = self.curr.right
            inorder(node.right)
        dummy = TreeNode(-1)
        self.curr = dummy
        inorder(root)
        return dummy.right