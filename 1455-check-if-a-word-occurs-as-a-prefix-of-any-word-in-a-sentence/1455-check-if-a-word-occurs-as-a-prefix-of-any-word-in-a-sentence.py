class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence, searchWord_len  = sentence.split(), len(searchWord)
        for index, word in enumerate(sentence):
            if word[:searchWord_len] == searchWord:
                return index + 1
        return -1