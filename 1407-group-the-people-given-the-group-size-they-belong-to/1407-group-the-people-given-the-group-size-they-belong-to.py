class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        dictionary = defaultdict(list)
        output = []
        for i in range(len(groupSizes)):
            dictionary[groupSizes[i]].append(i)
            if len(dictionary[groupSizes[i]]) == groupSizes[i]:
                output.append(dictionary[groupSizes[i]])
                dictionary[groupSizes[i]] = []
        return output