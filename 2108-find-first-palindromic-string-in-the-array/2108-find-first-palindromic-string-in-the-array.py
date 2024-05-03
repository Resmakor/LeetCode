class Solution(object):
    def ifPalindrome(self, word):
        size = len(word)
        for i in range(size // 2):
            if word[i] != word[size - 1 - i]:
                return False
        return True
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if self.ifPalindrome(word):
                return word
        return ""