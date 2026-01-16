class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        max_score = -1
        best_divisor = float('inf')
        for d in set(divisors):
            current_score = sum(1 for n in nums if n % d == 0)
            if current_score > max_score:
                max_score = current_score
                best_divisor = d
            elif current_score == max_score:
                best_divisor = min(best_divisor, d)
        return best_divisor