from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda x: (x[1] * (-1), x[0]))
        for key, value in counter:
            if key % 2 == 0:
                return key
        return -1
        