class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.split()
        output = []
        for i in range(len(text) - 1):
            if text[i] == first and text[i + 1] == second:
                if i + 2 < len(text):
                    output.append(text[i + 2])
        return output