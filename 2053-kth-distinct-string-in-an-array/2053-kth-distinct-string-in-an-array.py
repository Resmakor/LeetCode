class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        distinct = []
        for element in arr:
            if arr.count(element) == 1:
                distinct.append(element)
        if len(distinct) < k:
            return ""
        return distinct[k - 1]