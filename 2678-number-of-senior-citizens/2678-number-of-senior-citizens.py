class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        output = 0
        for person in details:
            if int(person[-4:-2]) > 60:
                output += 1
        return output