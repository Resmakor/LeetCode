class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        items = items1 + items2
        output = {}
        for element in items:
            if element[0] not in output.keys():
                output[element[0]] = element[1]
            else:
                output[element[0]] += element[1]
        output = output.items()
        output.sort(key=lambda element: element[0])
        return output