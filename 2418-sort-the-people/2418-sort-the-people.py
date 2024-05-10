class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        output = []
        sorted_heights = sorted(heights, reverse=True)
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]
        for element in sorted_heights:
            output.append(people[element])
        return output