class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            maxim = max(nums[0 : i + 1])
            minim = min(nums[i::])
            if (maxim - minim) <= k:
                return i
        return -1