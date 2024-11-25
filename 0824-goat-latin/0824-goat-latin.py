class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        sentence = sentence.split(' ')
        output = []
        for index, word in enumerate(sentence):
            new_word = word
            if word[0].lower() in vowels:
                new_word += "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            new_word += 'a' * (index + 1)
            output.append(new_word)
        return ' '.join(output)