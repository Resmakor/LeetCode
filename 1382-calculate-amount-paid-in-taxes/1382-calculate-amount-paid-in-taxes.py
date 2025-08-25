class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        output = 0
        prev_income = 0
        for i in range(len(brackets)):
            diff = brackets[i][0] - prev_income
            if diff > income:
                output += income * brackets[i][1] / 100.00
                income = 0
            else:
                output += diff * brackets[i][1] / 100.00
                income -= diff
            prev_income = brackets[i][0]
            if income == 0:
                return output