class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = []
        output = []
        for element in nums:
            if element not in visited:
                visited.append(element)
            else:
                output.append(element)
        return output