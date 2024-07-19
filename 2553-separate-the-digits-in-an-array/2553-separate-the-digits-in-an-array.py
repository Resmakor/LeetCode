class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums:
            str_num = str(num)
            if len(str_num) > 1:
                output.extend([int(element) for element in list(str_num)])
            else:
                output.append(num)
        return output