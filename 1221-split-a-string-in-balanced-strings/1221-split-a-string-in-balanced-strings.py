class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        output = 0
        for element in s:
            if element == 'R':
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                output += 1
        return output