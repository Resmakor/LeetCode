class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            condition_1 = flowerbed[i] == 0
            condition_2 = i == 0 or flowerbed[i - 1] == 0
            condition_3 = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if condition_1 and condition_2 and condition_3:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False