class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = list()
        for word in words:
            if output and sorted(output[-1]) == sorted(word):
                continue
            output.append(word)
        return output