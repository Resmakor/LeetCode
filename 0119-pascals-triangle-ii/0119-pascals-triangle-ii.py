class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1]
        for k in range(1, rowIndex + 1):
            output.append(output[-1] * (rowIndex - k + 1) // k)
        return output