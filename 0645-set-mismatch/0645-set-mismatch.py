class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        duplicate = -1
        current_sum = 0
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
                current_sum += num 
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - current_sum
        return [duplicate, missing]