class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4]) + 1): 
                output.append(str(chr(i)) + str(j))
        return output