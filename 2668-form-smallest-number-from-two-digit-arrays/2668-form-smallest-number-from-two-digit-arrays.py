class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        min1, min2 = min(nums1), min(nums2)
        set1, set2 = set(nums1), set(nums2)
        intersect = set1.intersection(set2)
        if intersect:
            min_common_element = min(intersect)
            if min(min1, min2) * 10 + max(min1, min2) >= min_common_element:
                return min_common_element
        return min(min1, min2) * 10 + max(min1, min2)