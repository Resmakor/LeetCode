class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        output = 0
        for element in words:
            if element in s[0:len(element)]:
                output += 1
        return output