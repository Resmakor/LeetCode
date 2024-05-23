class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        first_num = ""
        second_num = ""
        third_num = ""
        for character in firstWord:
            first_num += str(ord(character) - 97)
        for character in secondWord:
            second_num += str(ord(character) - 97)
        for character in targetWord:
            third_num += str(ord(character) - 97)
            
        if first_num == "":
            first_num = 0
        else:
            first_num = int(first_num)
        if second_num == "":
            second_num = 0
        else:
            second_num = int(second_num)
        if third_num == "":
            third_num = 0
        else:
            third_num = int(third_num)
        return first_num + second_num == third_num