class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = -1, len(nums)
        while True:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid
            if nums[mid] == target:
                return mid
            if left + 1 == right:
                return left + 1
            
