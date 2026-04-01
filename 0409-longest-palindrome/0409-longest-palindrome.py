class Solution:
    def longestPalindrome(self, s: str) -> int:
        output = 0
        isOdd = False
        counter = Counter(s)
        for key in counter:
            if counter[key] % 2 == 0:
                output += counter[key]
            else:
                isOdd = True
                output += counter[key] - 1
        if isOdd:
            return output + 1
        return output