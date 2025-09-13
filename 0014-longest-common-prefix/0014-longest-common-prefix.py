class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return output
            output += first[i]
        return output