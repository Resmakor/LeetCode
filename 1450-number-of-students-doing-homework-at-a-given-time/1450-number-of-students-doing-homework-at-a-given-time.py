class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        output = 0
        students_len = len(startTime)
        for i in range(students_len):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                output += 1
        return output