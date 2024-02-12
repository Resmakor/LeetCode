class Solution(object):
    def addBinary(self, a, b):
        if (a == "0" and b == "0"):
            return "0"
        c = int(a, 2) + int(b, 2)
        return bin(c).lstrip('0b')
        