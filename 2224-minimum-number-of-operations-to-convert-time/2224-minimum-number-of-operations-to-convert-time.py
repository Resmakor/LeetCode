class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        output = 0
        current_minutes = int(current[0:2]) * 60 + int(current[3:5])
        correct_minutes = int(correct[0:2]) * 60 + int(correct[3:5])
        difference = correct_minutes - current_minutes
        for i in (60, 15, 5, 1):
            if difference // i != 0:
                output += difference // i
                difference %= i
        return output