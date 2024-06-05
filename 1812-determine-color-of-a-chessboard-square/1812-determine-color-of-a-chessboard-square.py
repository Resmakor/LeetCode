class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        odd = ['a', 'c', 'e', 'g']
        even = ['b', 'd', 'f', 'h']
        if coordinates[0] in odd:
            if int(coordinates[1]) % 2 == 1:
                return False
            return True
        if coordinates[0] in even:
             if int(coordinates[1]) % 2 == 0:
                return False
             return True