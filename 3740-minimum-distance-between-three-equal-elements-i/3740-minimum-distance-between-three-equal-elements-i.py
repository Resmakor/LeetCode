class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minim = math.inf
        hasGoodTuple = False
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[j] != nums[i]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[j] == nums[k]:
                        hasGoodTuple = True
                        minim = min(abs(i - j) + abs(j - k) + abs(k - i), minim)
        if not hasGoodTuple:
            return -1
        return minim