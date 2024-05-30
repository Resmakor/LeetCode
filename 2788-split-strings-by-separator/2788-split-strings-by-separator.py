class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        output = []
        for word in words:
            splitted = word.split(separator)
            splitted_not_null = [splitted_word for splitted_word in splitted if splitted_word != ""]
            output.extend(splitted_not_null)
        return output