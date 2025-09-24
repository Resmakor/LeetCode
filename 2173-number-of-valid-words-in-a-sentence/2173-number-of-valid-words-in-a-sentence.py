class Solution(object):
    def isValid(self, word):
        hyphen_count, punct_count = 0, 0
        for i in range(len(word)):
            if word[i] >= '0' and word[i] <= '9':
                return False
            if word[i] == '-':
                if i == 0 or i == len(word) - 1 or hyphen_count >= 1:
                    return False
                if (word[i - 1] < 'a' or word[i - 1] > 'z') or (word[i + 1] < 'a' or word[i + 1] > 'z'):
                    return False
                else:
                    hyphen_count += 1
            if (word[i] == '!' or word[i] == '.' or word[i] == ','):
                if i != len(word) - 1 or punct_count >= 1:   
                    return False
                else:
                    punct_count += 1
        return True
                
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        output = 0
        words = sentence.split()
        for word in words:
            if self.isValid(word):
                output += 1
        return output