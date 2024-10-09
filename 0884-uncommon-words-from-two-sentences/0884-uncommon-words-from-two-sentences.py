class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        output = []
        s1 = s1.split()
        s2 = s2.split()
        two_sentences = s1 + s2
        dictionary = {}
        for word in two_sentences:
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1
        for word, count in dictionary.items():
            if count == 1:
                output.append(word)
        return output