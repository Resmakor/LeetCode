class MyHashSet(object):

    def __init__(self):
        self.hashSet = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hashSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)