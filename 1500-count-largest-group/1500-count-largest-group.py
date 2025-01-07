class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        frequency = {}
        max_size, output = 0, 0
        for index in range(1, n + 1):
            digit_sum = sum([int(i) for i in str(index)])
            if digit_sum not in frequency.keys():
                frequency[digit_sum] = [index]
            else:
                frequency[digit_sum].append(index)
            if len(frequency[digit_sum]) > max_size:
                max_size = len(frequency[digit_sum])
        for element in frequency:
            if len(frequency[element]) == max_size:
                output += 1
        return output
            