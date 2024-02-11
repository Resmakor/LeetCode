class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        x_n = x / 2
        for i in range(2 * len(str(x))):
            x_n1 = 0.5 * (x_n + (x / x_n))
            x_n = x_n1
        return int(x_n)
            
        
        