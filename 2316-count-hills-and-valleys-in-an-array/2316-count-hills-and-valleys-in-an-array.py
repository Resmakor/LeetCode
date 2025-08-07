class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        output, unique_nums = 0, [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                unique_nums.append(nums[i])
        nums = unique_nums
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                output += 1
            if nums[i] < nums[i + 1] and nums[i] < nums[i - 1]:
                output += 1
        return output