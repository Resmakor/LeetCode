class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels, r_vowels = ['a', 'e', 'i', 'o', 'u'], []
        for index, char in enumerate(s):
            if char.lower() in vowels:
                r_vowels.append(index)
        r_size, s = len(r_vowels), list(s)
        for i in range(r_size // 2):
            print(s[r_vowels[i]], s[r_vowels[r_size - 1 - i]])
            s[r_vowels[i]], s[r_vowels[r_size - 1 - i]] = s[r_vowels[r_size - 1 - i]], s[r_vowels[i]]
        return ''.join(s)
