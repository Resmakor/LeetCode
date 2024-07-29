class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        for element in arr2:
            i = 0
            while i < len(arr1):
                if arr1[i] == element:
                    output.append(element)
                    arr1.pop(i)
                else:
                    i += 1
        arr1.sort()
        output.extend(arr1)
        return output