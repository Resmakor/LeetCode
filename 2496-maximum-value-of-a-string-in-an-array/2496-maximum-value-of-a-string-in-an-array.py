class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        maximum_value = 0
        for word in strs:
            characters = False
            digits = False
            for character in word:
                if character >= 'a' and character <= 'z':
                    characters = True
                elif character >= '0' and character <= '9':
                    digits = True
            if (characters and digits or characters) and len(word) > maximum_value:
                maximum_value = len(word)
            elif not characters and digits and int(word) > maximum_value:
                maximum_value = int(word)
        return maximum_value