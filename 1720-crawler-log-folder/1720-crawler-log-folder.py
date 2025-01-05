class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        output = 0
        for log in logs:
            if log == "../":
                if output != 0:
                    output -= 1
            elif log == './':
                continue
            else:
                output += 1
        return output
