class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        apple_sum = sum(apple)
        capacity.sort()
        output, current_sum = 0, 0
        i = len(capacity) - 1
        while current_sum < apple_sum:
            current_sum += capacity[i]
            i -= 1
            output += 1
        return output