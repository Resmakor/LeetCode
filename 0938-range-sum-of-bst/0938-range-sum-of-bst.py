# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return 0
        if root.left == None and root.right == None:
            if root.val >= low and root.val <= high:
                return root.val
        elif root.left == None and root.right != None:
            if root.val >= low and root.val <= high:
                return self.rangeSumBST(root.right, low, high) + root.val
            return self.rangeSumBST(root.right, low, high)
        elif root.left != None and root.right == None:
            if root.val >= low and root.val <= high:
                return self.rangeSumBST(root.left, low, high) + root.val
            return self.rangeSumBST(root.left, low, high)
        if root.val >= low and root.val <= high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)