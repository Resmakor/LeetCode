class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        counter = 0
        for word in words:
            not_allowed = False
            for letter in word:
                if letter not in allowed:
                    not_allowed = True
                    break
            if not not_allowed:
                counter += 1
        return counter