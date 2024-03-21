class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique = set(arr)
        dict_arr = {}
        for element in unique:
            dict_arr[element] = 0
        for element in arr:
            dict_arr[element] += 1
        occurrences = []
        for value in dict_arr.values():
            occurrences.append(value)
        if len(set(occurrences)) == len(occurrences):
            return True
        return False
                