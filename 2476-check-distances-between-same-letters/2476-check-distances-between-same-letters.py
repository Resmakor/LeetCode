class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        dictionary = {}
        for index, letter in enumerate(s):
            if letter not in dictionary.keys():
                dictionary[letter] = index
            else:
                dictionary[letter] = index - dictionary[letter] - 1
        for key, value in dictionary.items():
            if dictionary[key] != distance[ord(key) - 97]:
                return False
        return True