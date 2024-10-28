class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_pivot = 0
        right_pivot = len(s) - 1
        s = list(s)
        while left_pivot < right_pivot:
            if s[left_pivot] < s[right_pivot]:
                s[right_pivot] = s[left_pivot]
            if s[left_pivot] > s[right_pivot]:
                s[left_pivot] = s[right_pivot]
            left_pivot += 1
            right_pivot -= 1
        return ''.join(s)