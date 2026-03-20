import math
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        curr_min, curr_index = math.inf, -1
        for index, num in enumerate(capacity):
            if num == itemSize:
                return index
            if num > itemSize and num < curr_min:
                curr_min = min(num, curr_min)
                curr_index = index
        return curr_index