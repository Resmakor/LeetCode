class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_copy = nums
        while len(nums) >= 1:
            if nums[len(nums) // 2] > target:
                nums = nums[0:len(nums) // 2]
            elif nums[len(nums) // 2] < target:
                nums = nums[len(nums) // 2 + 1:]
            else:
                return nums_copy.index(nums[len(nums) // 2])
        return -1