class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary, output = {}, -1
        for index, char in enumerate(s):
            if char not in dictionary.keys():
                dictionary[char] = [index]
            else:
                dictionary[char].append(index)
        for char in dictionary:
            minim, maxim = min(dictionary[char]), max(dictionary[char])
            if maxim != minim and maxim - minim - 1 > output:
                output = maxim - minim - 1
        return output