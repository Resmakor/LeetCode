class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        output = 0
        for num1 in arr1:
            flag = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = False
                    break
            if flag:
                output += 1
        return output
