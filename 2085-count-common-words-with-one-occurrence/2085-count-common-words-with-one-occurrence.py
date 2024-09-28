class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        output = 0
        if len(words1) <= len(words2):
            for element in words2:
                if words1.count(element) == 1 and words2.count(element) == 1:
                    output += 1
        else:
            for element in words1:
                if words1.count(element) == 1 and words2.count(element) == 1:
                    output += 1
        return output
                