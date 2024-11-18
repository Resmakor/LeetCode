class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return [0] * len(code)
        output = []
        for i in range(len(code)):
            element_sum = 0
            for j in range(abs(k)):
                if k < 0:
                    element_sum += code[i - 1 - j]
                elif i + j + 1 <= len(code) - 1:
                    element_sum += code[i + j + 1]
                else:
                    element_sum += code[i + j + 1 - len(code)]
            output.append(element_sum)
        return output