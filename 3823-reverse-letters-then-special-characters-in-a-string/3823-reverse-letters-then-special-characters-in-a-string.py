class Solution:
    def reverseByType(self, s: str) -> str:
        letters, special = "", ""
        for char in s:
            if char.isalpha():
                letters = char + letters
            else:
                special = char + special
        l_count, s_count = 0, 0
        output = ""
        for char in s:
            if char.isalpha():
                output += letters[l_count]
                l_count += 1
            else:
                output += special[s_count]
                s_count += 1
        return output