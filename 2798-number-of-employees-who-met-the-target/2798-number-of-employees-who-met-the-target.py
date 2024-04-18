class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        counter = 0
        for employee in hours:
            if employee >= target:
                counter += 1
        return counter