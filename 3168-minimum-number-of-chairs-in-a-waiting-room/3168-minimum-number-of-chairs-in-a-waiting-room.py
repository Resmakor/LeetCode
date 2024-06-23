class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_chairs = 0
        current_chairs = 0
        for element in s:
            if element == 'E':
                current_chairs += 1
            elif element == 'L':
                current_chairs -= 1
            if current_chairs > min_chairs:
                min_chairs = current_chairs
        return min_chairs