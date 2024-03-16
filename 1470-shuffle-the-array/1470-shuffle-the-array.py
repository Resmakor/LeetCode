class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[n + i])
        return new_list