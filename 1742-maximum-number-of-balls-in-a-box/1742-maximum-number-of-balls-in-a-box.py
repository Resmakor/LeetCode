class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            digits_sum = sum([int(num_string) for num_string in list(str(i))])
            if digits_sum in boxes.keys():
                boxes[digits_sum] += 1
            elif digits_sum not in boxes.keys():
                boxes[digits_sum] = 1
        return max(boxes.values())