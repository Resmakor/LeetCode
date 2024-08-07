class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_reversed = [word[::-1] for word in words]
        arr_size = len(words)
        forbidden = []
        for i in range(arr_size):
            for j in range(i + 1, arr_size):
                if words[i] == words_reversed[j] and [i, j] not in forbidden:
                    forbidden.append([i, j])
                    break
        return len(forbidden)
        