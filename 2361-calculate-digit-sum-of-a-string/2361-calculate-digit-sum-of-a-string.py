class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while k < len(s):
            new_s, temp = "", 0
            for i in range(len(s)):
                temp += int(s[i])
                if (i + 1) % k == 0 or i + 1 == len(s):
                    new_s += str(temp)
                    temp = 0
            s = new_s
        return s
