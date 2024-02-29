class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if s == goal:
            return True
        first_string = s
        while (1):
            letter = s[0]
            s = s[1:]
            s += letter
            if s == goal:
                return True
            elif first_string == s:
                return False
            