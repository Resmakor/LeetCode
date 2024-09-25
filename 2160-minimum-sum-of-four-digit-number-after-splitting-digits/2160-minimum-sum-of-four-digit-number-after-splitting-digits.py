class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = ''.join(sorted(str(num)))
        pair1 = num[0] + num[2]
        pair2 = num[1] + num[3]
        return int(pair1) + int(pair2)