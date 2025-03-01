class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        g_counter, output = 0, 0
        for i in range(len(s)):
            if s[i] >= g[g_counter]:
                output += 1
                g_counter += 1
            if g_counter == len(g):
                return output
        return output
