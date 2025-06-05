class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = []
        for i in range(len(nums)):
            if sum(int(x) for x in str(nums[i])) == i:
                output.append(i)
        if len(output) == 0:
            return -1
        return min(output)
        