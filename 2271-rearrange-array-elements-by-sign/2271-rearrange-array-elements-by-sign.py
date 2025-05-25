class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive, negative, output = [], [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        for i in range(len(positive)):
            output.append(positive[i])
            output.append(negative[i])
        return output