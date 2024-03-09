class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        new_s = ""
        for i in range(len(indices)):
            new_s += s[indices.index(i)]
        return new_s