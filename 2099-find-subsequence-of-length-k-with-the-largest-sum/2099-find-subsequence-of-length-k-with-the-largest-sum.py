class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_sorted = sorted(nums)[len(nums) - k:]
        output = []
        for num in nums:
            if num in nums_sorted:
                output.append(num)
                nums_sorted.remove(num)
            if len(nums_sorted) == 0:
                return output
        return output