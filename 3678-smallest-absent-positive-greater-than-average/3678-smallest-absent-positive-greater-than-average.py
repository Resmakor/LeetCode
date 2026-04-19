class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums) / len(nums)
        nums_set = set(nums)
        candidate = max(math.floor(average) + 1, 1)
        while True:
            if candidate not in nums_set:
                return candidate
            candidate += 1