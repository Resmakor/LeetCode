class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums) - 1):
            average = (sum(nums[i + 1:])) / (len(nums) - i - 1)
            if nums[i] > average:
                output += 1
        return output