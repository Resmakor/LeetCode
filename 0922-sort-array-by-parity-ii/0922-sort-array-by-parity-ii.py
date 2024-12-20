class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_pivot, odd_pivot = 0, 0
        even, odd = [], []
        output = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(nums)):
            if i % 2 == 0:
                output.append(even[even_pivot])
                even_pivot += 1
            else:
                output.append(odd[odd_pivot])
                odd_pivot += 1
        return output
                