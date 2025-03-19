# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = []
    def dfs(self, node, path):
            if node == None:
                return
            path += str(node.val)
            if node.left == None and node.right == None:
                self.result.append(path)
            else:
                self.dfs(node.left, path + '->')
                self.dfs(node.right, path + '->')
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        self.dfs(root, '')
        return self.result

            
