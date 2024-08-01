class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        sorted_boxes = sorted(boxTypes, key=itemgetter(1), reverse=True)
        output = 0
        for element in sorted_boxes:
            if truckSize - element[0] >= 0:
                output += element[0] * element[1]
                truckSize -= element[0]
            else:
                output += (truckSize % element[0]) * element[1]
                break
            if truckSize == 0:
                break
        return output
            