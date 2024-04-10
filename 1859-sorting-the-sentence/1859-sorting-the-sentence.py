class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        s_list = [''] * len(words)
        for word in words:
            s_list[int(word[-1]) - 1] = str(word[:-1])
        output = ""
        for word in s_list:
            output += word + ' '
        return output[:-1]