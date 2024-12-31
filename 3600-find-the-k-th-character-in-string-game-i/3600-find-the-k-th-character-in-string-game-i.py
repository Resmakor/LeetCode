class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        words = "a"
        while len(words) < k:
            for element in words:
                if ord(element) + 1 > ord('z'):
                    words += 'z'
                else:
                    words += chr(ord(element) + 1)
        return words[k - 1]
