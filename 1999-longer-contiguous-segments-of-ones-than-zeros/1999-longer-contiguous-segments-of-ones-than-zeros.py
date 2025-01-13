class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        longest_1, longest_0 = 0, 0
        temp_1, temp_0 = 0, 0
        for element in s:
            if element == '1':
                if temp_0 > longest_0:
                    longest_0 = temp_0
                temp_0 = 0
                temp_1 += 1
            elif element == '0':
                if temp_1 > longest_1:
                    longest_1 = temp_1
                temp_1 = 0
                temp_0 += 1
        if temp_1 > longest_1:
            longest_1 = temp_1
        if temp_0 > longest_0:
            longest_0 = temp_0
        return longest_1 > longest_0