class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        output = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if sorted(set(words[i])) == sorted(set(words[j])):
                    output += 1
        return output