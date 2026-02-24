class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding_window = set()
        for i in range(len(nums)):
            if i > k:
                sliding_window.remove(nums[i - k - 1])
            if nums[i] in sliding_window:
                return True
            sliding_window.add(nums[i])
        return False
