class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        hours_size = len(hours)
        output = 0
        for i in range(hours_size):
            for j in range(i + 1, hours_size):
                if (hours[i] + hours[j]) % 24 == 0:
                    output += 1
        return output