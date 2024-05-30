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
            not_null = [splitted_word for splitted_word in splitted if splitted_word != ""]
            output.extend(not_null)
        return output