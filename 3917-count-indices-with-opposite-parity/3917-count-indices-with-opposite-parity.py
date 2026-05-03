class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd = even = 0
        output = []
        for i in reversed(nums):
            if i % 2 == 0:
                even += 1
                output.append(odd)
            else:
                odd += 1
                output.append(even)
        return output[::-1]
