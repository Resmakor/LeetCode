class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        output = 0
        for word in words:
            flag = True
            for word_char in word:
                if word.count(word_char) > chars.count(word_char):
                    flag = False
                    break
            if flag:
                output += len(word)
        return output