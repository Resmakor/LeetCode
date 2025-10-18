class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        output = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] not in output.keys():
                    output[nums[i + 1]] = 1
                else:
                    output[nums[i + 1]] += 1
        return max(output.items(), key=lambda x: x[1])[0]

        