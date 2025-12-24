class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        apples = sum(apple)
        capacity = sorted(capacity, reverse=True)
        curr_sum, output = 0, 0
        for cap in capacity:
            if curr_sum >= apples:
                return output
            else:
                curr_sum += cap
                output += 1
        return output
