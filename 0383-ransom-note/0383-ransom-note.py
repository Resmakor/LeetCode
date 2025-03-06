from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_c, magazine_c = Counter(ransomNote), Counter(magazine)
        for element in ransom_c:
            if magazine_c[element]:
                if ransom_c[element] > magazine_c[element]:
                    return False
            else:
                return False
        return True