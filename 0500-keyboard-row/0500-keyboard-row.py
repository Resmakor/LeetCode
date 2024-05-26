class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        output = []
        first_flag = True
        second_flag = True
        third_flag = True
        for word in words:
            for letter in word:
                if letter.lower() not in first_row:
                    first_flag = False
                if letter.lower() not in second_row:
                    second_flag = False
                if letter.lower() not in third_row:
                    third_flag = False
            if first_flag or second_flag or third_flag:
                output.append(word)
            first_flag = True
            second_flag = True
            third_flag = True
        return output