class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = length >= 10000 or width >= 10000 or height >= 10000
        isBulky = isBulky or length * width * height >= 1000000000
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return "Both"
        if not isBulky and not isHeavy:
            return "Neither"
        if isBulky and not isHeavy:
            return "Bulky"
        if isHeavy and not isBulky:
            return "Heavy"