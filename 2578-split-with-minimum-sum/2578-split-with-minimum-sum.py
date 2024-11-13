class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_nums = [element for element in str(num)]
        str_nums.sort()
        str_num1, str_num2 = "", ""
        for i in range(len(str_nums)):
            if i % 2 == 0:
                str_num1 += str_nums[i]
            else:
                str_num2 += str_nums[i]
        return int(str_num1) + int(str_num2)