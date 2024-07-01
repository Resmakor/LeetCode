class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for element in nums:
            if element % 3 == 0:
                continue
            elif (element + 1) % 3 == 0 or (element - 1) % 3 == 0:
                output += 1
            else:
                output += 2
        return output