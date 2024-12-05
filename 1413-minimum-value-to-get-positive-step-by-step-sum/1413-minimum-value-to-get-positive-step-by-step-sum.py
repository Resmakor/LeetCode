class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        start_value = max(1 - nums[0], 1)
        while True:
            current_sum, stopped = start_value, False
            for num in nums:
                if num + current_sum < 1:
                    start_value += 1
                    stopped = True
                    break
                else:
                    current_sum += num
            if not stopped:
                return start_value