class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        for character in words[0]:
            character_appeared = True
            for i in range(1, len(words)):
                if character not in words[i]:
                    character_appeared = False
                    break
                else:
                    words[i] = words[i].replace(character, "", 1)
            if character_appeared:
                output.append(character)
        return output