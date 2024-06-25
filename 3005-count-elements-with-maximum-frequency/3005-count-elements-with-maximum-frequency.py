class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequencies = {}
        max_freq = 0
        output = 0
        for element in nums:
            if element not in frequencies.keys():
                frequencies[element] = 1
            else:
                frequencies[element] += 1
        for key in frequencies.keys():
            if frequencies[key] > max_freq:
                max_freq = frequencies[key]
        for key in frequencies.keys():
            if frequencies[key] == max_freq:
                output += frequencies[key]
        return output