class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_size = len(nums)
        counter = 0
        for a in range(nums_size):
            for b in range(a + 1, nums_size):
                for c in range(b + 1, nums_size):
                    for d in range(c + 1, nums_size):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            counter += 1
        return counter