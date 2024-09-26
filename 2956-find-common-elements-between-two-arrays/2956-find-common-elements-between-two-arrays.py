class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common_set = set()
        output = [0, 0]
        for element in nums1:
            if element in nums2:
                common_set.add(element)
                output[0] += 1
        for element in nums2:
            if element in common_set:
                output[1] += 1
        return output