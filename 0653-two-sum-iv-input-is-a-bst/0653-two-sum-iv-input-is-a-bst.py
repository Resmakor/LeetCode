# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_to_list(self, root):
        if root.left == None and root.right == None:
            return [root.val]
        if root.left != None and root.right == None:
            return [root.val] + self.tree_to_list(root.left) 
        if root.left == None and root.right != None:
            return [root.val] + self.tree_to_list(root.right)
        return [root.val] + self.tree_to_list(root.left) + self.tree_to_list(root.right)
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        tree_list = self.tree_to_list(root)
        for i in range(len(tree_list)):
            for j in range(i + 1, len(tree_list)):
                if tree_list[i] + tree_list[j] == k:
                    return True
        return False
