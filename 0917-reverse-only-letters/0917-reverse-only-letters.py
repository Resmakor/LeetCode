class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        output, reversed_letters, counter = "", "", 0
        for element in s[::-1]:
            if element >= 'a' and element <= 'z' or element >= 'A' and element <= 'Z':
                reversed_letters += element
        for i in range(len(s)):
            if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z':
                output += reversed_letters[counter]
                counter += 1
            else:
                output += s[i]   
        return output