class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = 0
        alt_max = 0
        for element in gain:
            alt += element
            if alt > alt_max:
                alt_max = alt
        return alt_max