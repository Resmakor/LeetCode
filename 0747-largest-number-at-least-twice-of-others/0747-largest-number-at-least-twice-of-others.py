class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums[-1] >= 2 * sorted_nums[-2]:
             for i in range(len(nums)):
                if nums[i] == sorted_nums[-1]:
                    return i
        return -1