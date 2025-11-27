class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        curr_line, lines = 0, 1
        for i in range(len(s)):
            char = widths[ord(s[i]) - 97]
            if curr_line + char > 100:
                lines += 1
                curr_line = char
            else:
                curr_line += char
        return [lines, curr_line]