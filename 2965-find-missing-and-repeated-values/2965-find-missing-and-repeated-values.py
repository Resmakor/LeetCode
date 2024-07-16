class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        one_list = []
        for row in grid:
            one_list.extend(row)
            
        # Finding duplicate
        seen = []
        for element in one_list:
            if element in seen:
                duplicate = element
                break
            else:
                seen.append(element)
                
        # Finding missing number
        correct_list = set(range(1, len(one_list) + 1))
        unique_values = set(one_list)
        missing = list(correct_list.difference(unique_values))[0]
        
        return [duplicate, missing]