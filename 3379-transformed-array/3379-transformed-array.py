class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(nums[(i + nums[i]) % len(nums)])
        return output