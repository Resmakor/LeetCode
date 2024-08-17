import string
class Solution(object):
    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
    def find_jump_distance(self, letter, pointer):
        int_letter = ord(letter) - 97
        int_pointer = ord(pointer) - 97
        normal_move = abs(int_letter - int_pointer)
        backwards_move = 26 - normal_move
        return min(normal_move, backwards_move)
        
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        pointer = 'a'
        index = 0
        time = 0
        for letter in word:
            distance = self.find_jump_distance(letter, pointer)
            if self.alphabet[(index + distance) % 26] == letter:
                pointer = self.alphabet[(index + distance) % 26]
                index += distance
            else:
                pointer = self.alphabet[(index - distance) % 26]
                index -= distance
            time += abs(distance) + 1
        return time