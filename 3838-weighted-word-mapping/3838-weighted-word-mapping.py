class Solution:
    def mapWord(self, word, weights):
        mapped = 0
        for char in word:
            mapped += weights[ord(char) - 97]
        return mapped % 26
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        output = ""
        for word in words:
            output += chr(122 - self.mapWord(word, weights))
        return output