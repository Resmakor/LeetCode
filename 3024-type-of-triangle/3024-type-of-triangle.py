class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        if not (nums[0] + nums[1] > nums[2]):
            return "none"
        elif nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        elif (nums[0] == nums[1] and nums[2] != nums[1]) or (nums[1] == nums[2] and nums[0] != nums[1]):
            return "isosceles"
        elif (nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]):
            return "scalene"
        