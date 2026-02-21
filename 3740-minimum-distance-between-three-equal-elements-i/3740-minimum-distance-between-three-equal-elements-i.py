class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minim = math.inf
        hasGoodTuple = False
        values = {}
        for index, value in enumerate(nums):
            if value not in values:
                values[value] = [index]
            else:
                values[value].append(index)
            if len(values[value]) >= 3:
                hasGoodTuple = True
                i, j, k = values[value][-3], values[value][-2], values[value][-1]
                current_value = abs(i - j) + abs(j - k) + abs(k - i)
                minim = min(minim, current_value)
        if hasGoodTuple:
            return minim
        return -1