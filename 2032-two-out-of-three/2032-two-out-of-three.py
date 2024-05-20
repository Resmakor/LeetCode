class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        counter = []
        each_number = set(nums1 + nums2 + nums3)
        for element in each_number:
            if element in nums1 and element in nums2 or element in nums1 and element in nums3 or element in nums2 and element in nums3:
                counter.append(element)
        return counter