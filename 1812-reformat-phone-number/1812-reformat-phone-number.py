class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        output = []
        s = ""
        for char in number:
            if char != ' ' and char != '-':
                s += char
        while s:
            if len(s) == 2:
                output.append(s)
                break
            elif len(s) == 4:
                output.append(s[:2])
                output.append(s[2:])
                break
            else:
                output.append(s[:3])
                s = s[3:]
        return '-'.join(output)