class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        curr_string = ""
        for word in words:
            curr_string += word
            if curr_string == s:
                return True
            if len(curr_string) >= s:
                return False
        return False