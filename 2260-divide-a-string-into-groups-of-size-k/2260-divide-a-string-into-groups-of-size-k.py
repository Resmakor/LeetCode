class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        current_string, output = "", []
        for index, letter in enumerate(s):
            if index % k == 0 and index != 0:
                output.append(current_string)
                current_string = letter
            else:
                current_string += letter
        if len(current_string) != 0:
            current_string += fill * (k - len(current_string))
            output.append(current_string)
        return output
