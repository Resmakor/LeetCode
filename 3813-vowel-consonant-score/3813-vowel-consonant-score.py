class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v, c = 0, 0
        for char in s:
            if char >= '0' and char <= '9' or char == ' ':
                continue
            if char in vowels:
                v += 1
            else:
                c += 1
        if c > 0:
            return math.floor(v / c)
        return 0
        