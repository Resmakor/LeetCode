class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even, odd = [], []
        even_pivot, odd_pivot = 0, 0
        output = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        for i in range(len(nums)):
            if i % 2 == 0:
                output.append(even[even_pivot])
                even_pivot += 1
            else:
                output.append(odd[odd_pivot])
                odd_pivot += 1
        return output