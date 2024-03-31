class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        encrypted_sum = 0
        for element in nums:
            digits = [int(d) for d in str(element)]
            max_digit = max(digits)
            encrypted_sum += int(str(max_digit) * len(str(element)))
        return encrypted_sum