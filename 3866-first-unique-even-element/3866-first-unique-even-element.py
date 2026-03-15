class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen_twice = set()
        seen_once = []
        for num in nums:
            if num % 2 == 0:
                if num in seen_once:
                    seen_once.remove(num)
                    seen_twice.add(num)
                elif num not in seen_twice and num not in seen_once:
                    seen_once.append(num)
        if len(seen_once) > 0:
            return seen_once[0]
        return -1
                