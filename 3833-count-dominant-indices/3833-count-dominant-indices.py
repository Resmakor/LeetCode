class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        output = 0
        sum_n = sum(nums)
        division = len(nums)
        for i in range(len(nums) - 1):
            sum_n -= nums[i]
            division -= 1
            average = sum_n / division
            if nums[i] > average:
                output += 1
        return output