class Solution(object):
    def singleNumber(self, nums):
        for element in nums:
            if nums.count(element) == 1:
                return element
        
        