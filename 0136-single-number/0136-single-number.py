class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        length = len(nums)
        for i in range(length + 1):
            if i > 0 and i < length - 1 and length > 3:
                if nums[i] != nums[i + 1] and nums[i + 1] != nums[i + 2]:
                    return nums[i + 1]
                else:
                    i += 1
            if i == 0:
                if length == 1:
                    return nums[i]
                else:
                    if nums[i] != nums[i + 1]:
                        return nums[i]
            if i == length - 2:
                if nums[i] != nums[i + 1]:
                    return nums[i + 1]
        
        