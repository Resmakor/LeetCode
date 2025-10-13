class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        output = 0
        counter = Counter(nums)
        for key in counter:
            if counter[key] % k == 0:
                output += key * counter[key]
        return output