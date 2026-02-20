class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        output = []
        counter = Counter(bulbs)
        for key in counter:
            if counter[key] % 2 != 0:
                output.append(key)
        return sorted(output)