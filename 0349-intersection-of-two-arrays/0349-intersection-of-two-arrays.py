class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        unique = []
        for element in nums1:
            if element in nums2 and element not in unique:
                unique.append(element)
        return unique