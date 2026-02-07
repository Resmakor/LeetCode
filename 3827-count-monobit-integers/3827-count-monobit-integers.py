class Solution:
    def isMonobit(self, integer):
        if integer == 0:
            return True
        binary = str(bin(integer)).lstrip('0b')
        ones = binary.count('1')
        zeroes = len(binary) - ones
        return ones == 0 and zeroes != 0 or ones != 0 and zeroes == 0
    def countMonobit(self, n: int) -> int:
        output = 0
        for integer in range(0, n + 1):
            if self.isMonobit(integer):
                output += 1
        return output