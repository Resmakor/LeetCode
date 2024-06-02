class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        output = [first]
        for element in encoded:
            output.append(output[-1] ^ element)
        return output