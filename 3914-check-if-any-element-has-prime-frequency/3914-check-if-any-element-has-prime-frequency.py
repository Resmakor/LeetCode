class Solution(object):
    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        frequencies = Counter(nums)
        for frequency in frequencies.values():
            if self.isPrime(frequency):
                return True
        return False