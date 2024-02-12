class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 0:
            return [1]
        elif digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
            return digits
                
                
        