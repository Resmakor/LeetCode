class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        output = tasks[0][0] + tasks[0][1]
        for task in tasks:
            output = min(output, task[0] + task[1])
        return output