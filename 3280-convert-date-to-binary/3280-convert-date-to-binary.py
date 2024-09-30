class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        date_elements = date.split('-')
        output = ""
        for element in date_elements:
            output += bin(int(element)).lstrip('0b') + '-'
        return output[:-1]