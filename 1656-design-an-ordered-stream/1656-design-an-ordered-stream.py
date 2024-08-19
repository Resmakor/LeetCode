class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.n[idKey - 1] = value
        for i in range(idKey):
            if self.n[i] == None:
                return []
        output = []
        for i in range(self.ptr, len(self.n)):
            if self.n[i] != None:
                output.append(self.n[i])
                self.ptr += 1
            else:
                break
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)