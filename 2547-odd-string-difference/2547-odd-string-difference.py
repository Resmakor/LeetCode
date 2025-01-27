class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        arr = []
        for word in words:
            current_arr = []
            for i in range(len(word) - 1):
                current_arr.append(ord(word[i + 1]) - ord(word[i]))
            arr.append([current_arr, word])
        arr.sort()
        if arr[0][0] == arr[1][0]:
            return arr[-1][1]
        else:
            return arr[0][1]
    