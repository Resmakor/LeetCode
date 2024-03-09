class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        dictionary = {}
        counter = 0
        for indice in indices:
            dictionary[indice] = s[counter]
            counter += 1
        
        new_s = ""
        for i in range(len(indices)):
            new_s += dictionary[i]
        return new_s