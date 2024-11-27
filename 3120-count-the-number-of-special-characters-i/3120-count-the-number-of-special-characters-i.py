class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        output = 0
        big_counter = [0] * 26
        low_counter = [0] * 26
        for letter in word:
            if letter.isupper():
                big_counter[ord(letter) - 65] += 1
            else:
                low_counter[ord(letter) - 97] += 1
        for i in range(26):
            if big_counter[i] > 0 and low_counter[i] > 0:
                output += 1
        return output