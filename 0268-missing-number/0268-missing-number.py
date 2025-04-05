class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        whole_range = set(range(max(nums_set)))
        output_list = list(whole_range.difference(nums_set))
        if len(output_list) == 0:
            return max(nums_set) + 1
        return output_list[0]