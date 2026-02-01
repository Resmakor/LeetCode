class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_len = n - 1
        num_cycles = time // cycle_len
        rem = time % cycle_len
        if num_cycles % 2 == 0:
            return 1 + rem
        return n - rem