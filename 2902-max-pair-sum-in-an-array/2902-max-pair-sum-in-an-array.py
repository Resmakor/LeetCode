from collections import defaultdict
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = defaultdict(list)
        output = -1
        for num in nums:
            max_digit = max(str(num))
            digits[max_digit].append(num)
        for digit in digits:
            if len(digits[digit]) > 1:
                digits[digit].sort()
                output = max(output, digits[digit][-1] + digits[digit][-2])
        return output
