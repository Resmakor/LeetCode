class Solution(object):
    def ifPalindrome(self, word):
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - 1 - i]:
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