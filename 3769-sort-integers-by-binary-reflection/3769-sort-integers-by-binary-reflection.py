class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: (int(bin(x).lstrip('0b')[::-1], 2), x))