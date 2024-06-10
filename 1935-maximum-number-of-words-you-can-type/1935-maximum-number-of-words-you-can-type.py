class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        output = 0
        text_list = text.split()
        for word in text_list:
            broken = False
            for letter in word:
                if letter in brokenLetters:
                    broken = True
                    break
            if not broken:
                output += 1
        return output