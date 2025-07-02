class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        output = []
        increase, decrease = 0, len(s)
        for i in s:
            if i == 'I':
                output.append(increase)
                increase += 1
            elif i == 'D':
                output.append(decrease)
                decrease -= 1
        output.append(increase)
        return output