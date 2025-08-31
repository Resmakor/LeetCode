class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        friends = set(friends)
        output = []
        for o in order:
            if o in friends:
                output.append(o)
        return output