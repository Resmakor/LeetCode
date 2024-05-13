class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for element in nums:
            if element % 2 == 0:
                odd.append(element)
            else:
                even.append(element)
        return odd + even