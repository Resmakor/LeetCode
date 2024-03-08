class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = []
        new_title = ""
        for word in title.split():
            if len(word) == 2 or len(word) == 1:
                words.append(word.lower())
            else:
                word = word.lower()
                word = word[0].upper() + word[1:]
                words.append(word)
        new_title = " ".join(words)
        return new_title