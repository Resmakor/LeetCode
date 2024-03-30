class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_len = 0
        for sentence in sentences:
            arr = sentence.split(' ')
            if max_len < len(arr):
                max_len = len(arr)
        return max_len