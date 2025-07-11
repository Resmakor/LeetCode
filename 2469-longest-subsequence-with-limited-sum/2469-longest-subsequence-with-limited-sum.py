class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        output = []
        nums.sort()
        prefix_sums = [0] * len(nums)
        prefix_sums[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i]
        for query in queries:
            index = bisect.bisect_right(prefix_sums, query)
            output.append(index)
        return output