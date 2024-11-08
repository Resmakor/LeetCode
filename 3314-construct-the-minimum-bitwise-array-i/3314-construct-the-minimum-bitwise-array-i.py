class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums:
            found = False
            for i in range(1, num):
                if i | (i + 1) == num:
                    output.append(i)
                    found = True
                    break
            if not found:
                output.append(-1)
        return output
                