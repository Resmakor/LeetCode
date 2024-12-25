class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_sum, even_len = 0, 0
        for num in nums:
            if num % 6 == 0:
                even_sum += num
                even_len += 1
        if even_len == 0:
            return 0
        return int(even_sum / even_len)