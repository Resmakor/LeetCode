class Solution:
    def residuePrefixes(self, s: str) -> int:
        distinct_val = set()
        output = 0
        for index, char in enumerate(s):
            distinct_val.add(char)
            if (index + 1) % 3 == len(distinct_val):
                output += 1
        return output