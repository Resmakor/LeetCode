class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        pairs = 0
        leftover = 0
        counter = 0
        nums_size = len(nums)
        if nums_size == 1:
            return [0, 1]
        while counter < nums_size:
            if counter + 1 == nums_size:
                leftover += 1
                break
            if nums[counter] == nums[counter + 1]:
                pairs += 1
                counter += 1
            else:
                leftover += 1
            counter += 1
        return [pairs, leftover]