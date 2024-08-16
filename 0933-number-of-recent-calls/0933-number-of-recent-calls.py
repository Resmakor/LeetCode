class RecentCounter(object):

    def __init__(self):
        self.counter = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        output = 0
        self.counter.append(t)
        for element in self.counter[::-1]:
            if element >= t - 3000 and element <= t:
                output += 1
            else:
                return output
        return output


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)