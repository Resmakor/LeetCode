class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(int(operation))
        return sum(record)
                