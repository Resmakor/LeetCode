class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen, ans = [], []
        k = 0
        for num in nums:
            if num != -1:
                seen = [num] + seen
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1]) 
                else:
                    ans.append(-1)
        return ans
