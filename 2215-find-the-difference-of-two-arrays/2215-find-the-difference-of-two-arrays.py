class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        distinct_1 = set(nums1).difference(set(nums2))
        distinct_2 = set(nums2).difference(set(nums1))
        return [list(distinct_1), list(distinct_2)]
        
        