class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        array = []
        for index, word in enumerate(words):
            if x in word:
                array.append(index)
        return array