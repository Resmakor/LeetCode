class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strong_pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                if abs(num1 - num2) <= min(num1, num2):
                    strong_pairs.append([num1, num2])
        max_xor = 0
        for element in strong_pairs:
            pair_xor = element[0] ^ element[1]
            if pair_xor >= max_xor:
                max_xor = pair_xor
        return max_xor