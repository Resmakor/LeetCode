class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        output = 0
        while amount != [0, 0, 0]:
            amount.sort()
            if amount[1] != 0:
                amount[1] -= 1
                amount[2] -= 1
                output += 1
            else:
                output += amount[2]
                amount[2] = 0
        return output