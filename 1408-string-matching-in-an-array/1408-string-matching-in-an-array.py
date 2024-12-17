class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        for i in range(len(words)):
            for j in range(0, len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    output.append(words[i])
                    break
        return output