class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        i, j = min(start, destination), max(start, destination)
        return min(sum(distance[i:j]), sum(distance[:i]) + sum(distance[j:]))