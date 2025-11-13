class Solution(object):
    def min_pair(self, nums):
        n = len(nums)
        minim, min_index = sys.maxint, 0
        for i in range(n - 1):
            pair_sum = nums[i] + nums[i + 1]
            if minim > pair_sum:
                minim = pair_sum
                min_index = i
        return minim, min_index
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        while True:
            if nums == sorted(nums):
                return output
            minim, min_index = self.min_pair(nums)
            nums.pop(min_index + 1)
            nums.pop(min_index)
            nums.insert(min_index, minim)
            output += 1