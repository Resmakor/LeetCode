class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        withoutNonAlpha = []
        for char in s:
            if char.isalnum():
                withoutNonAlpha.append(char.lower())
        return withoutNonAlpha == withoutNonAlpha[::-1]