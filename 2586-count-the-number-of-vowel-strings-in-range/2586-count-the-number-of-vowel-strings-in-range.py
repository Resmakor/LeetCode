class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        output = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                output += 1
        return output