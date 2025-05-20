class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        output = []
        for i in range(len(boxes)):
            output.append(0)
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    output[i] += abs(i - j)
        return output