class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums_size = len(nums)
        if nums_size == 1 or nums_size == 0:
            return 0
        nums, output = sorted(nums), 100000
        for i in range(nums_size - k + 1):
            output = min(output, nums[i + k - 1] - nums[i])
        return output