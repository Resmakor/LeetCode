class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(s) != len(pattern):
            return False
        dictionary = defaultdict(list)
        for index, char in enumerate(pattern):
            dictionary[char].append(s[index])
        seen = []
        for key in dictionary:
            unique = list(set(dictionary[key]))
            if len(unique) > 1:
                return False
            if unique in seen:
                return False
            seen.append(unique)
        return True