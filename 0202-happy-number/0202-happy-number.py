class Solution(object):
    def isHappy(self, n):
        visited = set()
        while 1:
            if n == 1:
                return True
            elif n in visited:
                return False
            visited.add(n)
            temp = 0
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp

            
            
        