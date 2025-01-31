class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        target_dict, characters_dict = {}, {}
        for element in target:
            if element not in target_dict.keys():
                target_dict[element] = 1
            else:
                target_dict[element] += 1
        for letter in s:
            if letter in target_dict.keys():
                if letter not in characters_dict.keys():
                    characters_dict[letter] = 1
                else:
                    characters_dict[letter] += 1
        if len(characters_dict.keys()) != len(target_dict.keys()):
            return 0
        for key in characters_dict.keys():
            characters_dict[key] //= target_dict[key]
        return min(characters_dict.values())