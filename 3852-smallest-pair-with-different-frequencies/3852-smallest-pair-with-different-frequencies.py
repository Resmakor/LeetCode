class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = (Counter(nums))
        sorted_pairs = sorted(freq.items(), key=lambda x: x[0])
        first_val, first_freq = sorted_pairs[0]
        for val, freq in sorted_pairs[1:]:
            if freq != first_freq:
                return [first_val, val]
        return [-1, -1]