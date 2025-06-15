class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_sorted = sorted(score, reverse=True)
        dictionary, output = {}, []
        for index, element in enumerate(score_sorted):
            dictionary[element] = str(index + 1)
        for element in score:
            if dictionary[element] == '1':
                output.append('Gold Medal')
            elif dictionary[element] == '2':
                output.append('Silver Medal')
            elif dictionary[element] == '3':
                output.append('Bronze Medal')
            else:
                output.append(dictionary[element])
        return output
