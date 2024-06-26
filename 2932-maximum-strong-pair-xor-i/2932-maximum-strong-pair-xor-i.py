class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strong_pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    strong_pairs.append([nums[i], nums[j]])
        max_xor = 0
        for element in strong_pairs:
            pair_xor = element[0] ^ element[1]
            if pair_xor >= max_xor:
                max_xor = pair_xor
        return max_xor