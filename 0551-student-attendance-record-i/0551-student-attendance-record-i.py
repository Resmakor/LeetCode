class Solution:
    def checkRecord(self, s: str) -> bool:
        A, L = 0, 0
        for char in s:
            if char == 'A':
                A += 1
            if char == 'L':
                L += 1
                if L == 3:
                    return False
            else:
                L = 0
        return A < 2