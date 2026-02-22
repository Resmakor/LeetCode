class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        counter = 0
        for i in range(len(s)):
            if s[i] == '1':
                counter += 1
            else:
                break
        return not '1' in s[counter + 1:]