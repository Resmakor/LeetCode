class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = ""
        counter = 0
        for letter in str(num):
            if letter == '6' and counter != 1:
                str_num += "9"
                counter = 1
            else:
                str_num += letter
        return int(str_num)
                
            
            