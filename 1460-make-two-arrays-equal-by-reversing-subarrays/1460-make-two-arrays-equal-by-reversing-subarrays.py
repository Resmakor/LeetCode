class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        target.sort()
        if arr == target:
            return True
        return False