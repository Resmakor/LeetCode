class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = []
        twice = []
        for num in nums:
            if num not in once:
                once.append(num)
            elif num in once:
                twice.append(num)
        if len(twice) == 0:
            return 0
        if len(twice) == 1:
            return twice[0]
        output = 0
        for element in twice:
            output = output ^ element
        return output
            
            
        