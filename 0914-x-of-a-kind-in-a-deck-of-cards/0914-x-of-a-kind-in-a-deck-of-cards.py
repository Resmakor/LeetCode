class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*Counter(deck).values()) >= 2