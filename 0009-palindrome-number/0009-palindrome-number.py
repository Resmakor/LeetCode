class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x_size = len(x)
        for i in range(x_size / 2):
            if (x[i] != x[x_size - 1 - i]):
                return False
        return True
        