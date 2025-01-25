class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        arr_size, whole_time = len(timeSeries), 0
        if arr_size == 0:
            return 0
        for i in range(arr_size - 1):
            whole_time += min(timeSeries[i + 1] - timeSeries[i], duration)
        return whole_time + duration
        