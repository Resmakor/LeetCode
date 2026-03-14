class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        output = []
        temp = []
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if temp == []:
                    temp = [i, i + 1]
                else:
                    temp[1] = i + 1
            else:
                if temp != [] and temp[1] - temp[0] >= 2:
                    output.append(temp)
                temp = []
        if temp != [] and (temp[1] - temp[0] >= 2):
            output.append(temp)
        return output