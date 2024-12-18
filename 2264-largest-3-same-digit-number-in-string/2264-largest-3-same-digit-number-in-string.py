class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        counter, good_numbers = 1, []
        for i in range(len(num) - 1):
            if num[i] == num[i + 1]:
                counter += 1
            else:
                counter = 1
            if counter == 3:
                good_numbers.append([num[i]] * 3)
                counter = 1
        if len(good_numbers) == 0:
            return ""
        return ''.join(max(good_numbers))