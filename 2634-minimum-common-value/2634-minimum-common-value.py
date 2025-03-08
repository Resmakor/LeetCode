class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s_nums1, s_nums2 = set(nums1), set(nums2)
        diff = s_nums1.intersection(s_nums2)
        if len(diff) == 0:
            return -1
        return min(list(diff))