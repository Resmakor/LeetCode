class Solution(object):
    def __init__(self):
        self.mapping = defaultdict(list)

    def isOrdered(self, low, high):
            for i in range(min(len(low), len(high))):
                if self.mapping[low[i]] < self.mapping[high[i]]:
                    return True
                if self.mapping[low[i]] > self.mapping[high[i]]:
                    return False
            return len(low) <= len(high)
        
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for index, letter in enumerate(order):
            self.mapping[letter] = index
        for i in range(len(words) - 1):
            if not self.isOrdered(words[i], words[i + 1]):
                return False
        return True

        
        
        