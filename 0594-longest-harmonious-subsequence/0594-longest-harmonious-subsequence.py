class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = Counter(nums)
        output = 0
        for key in counter:
            if key + 1 in counter:
                output = max(counter[key] + counter[key + 1], output)
        return output
        