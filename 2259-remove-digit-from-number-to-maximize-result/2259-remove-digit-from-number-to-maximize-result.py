class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        output = ""
        for i in range(len(number)):
            if digit == number[i]:
                output = max(number[:i] + number[i + 1:], output)
        return output