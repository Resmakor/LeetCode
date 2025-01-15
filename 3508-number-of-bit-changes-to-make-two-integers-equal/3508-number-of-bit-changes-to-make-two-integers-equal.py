class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n < k:
            return -1
        output = 0
        n = str(bin(n).lstrip('0b'))
        k = str(bin(k).lstrip('0b'))
        k = '0' * (len(n) - len(k)) + k
        for i in range(len(n)):
            if n[i] != k[i] and n[i] == '1':
                output += 1
            elif n[i] == k[i]:
                continue
            else:
                return -1
        return output