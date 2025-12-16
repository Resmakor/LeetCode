class Solution(object):
    def __init__(self):
        self.operations = 0

    def trimStr(self, string):
        str_len = len(string)
        if str_len != self.min_len:
            self.operations += str_len - self.min_len
            string = string[:self.min_len]
        return string

    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        self.max_len = max(s1_len, s2_len, s3_len)
        self.min_len = min(s1_len, s2_len, s3_len)
        s1, s2, s3 = self.trimStr(s1), self.trimStr(s2), self.trimStr(s3)
        while len(s1) >= 1:
            if s1 == s2 == s3:
                return self.operations
            s1 = s1[:len(s1) - 1]
            s2 = s2[:len(s2) - 1]
            s3 = s3[:len(s3) - 1]
            self.operations += 3
        return -1