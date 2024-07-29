class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        for element in arr2:
            while element in arr1:
                output.append(element)
                arr1.remove(element)
        arr1.sort()
        output.extend(arr1)
        return output