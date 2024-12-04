class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return sorted(nums[0])
        output = set()
        for i in range(0, len(nums) - 1, 2):
            if i == 0:
                intersection = set(nums[i]).intersection(set(nums[i + 1]))
                output = intersection
            else:
                output = output.intersection(set(nums[i]))
        if len(nums) % 2 != 0:
            output = output.intersection(set(nums[-1]))
        return sorted(list(output))