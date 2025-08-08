class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        output = [pref[0]]
        for i in range(1, len(pref)):
            output.append(pref[i - 1] ^ pref[i])
        return output