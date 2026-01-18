from itertools import groupby
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        diffs = []
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff == 0:
                return False
            diffs.append(1 if diff > 0 else -1)
        unique = [k for k, g in groupby(diffs)]
        return unique == [1, -1, 1]