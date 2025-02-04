from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter1, counter2 = Counter(nums1), Counter(nums2)
        output = []
        for key in counter1:
            minimum = min(counter1[key], counter2[key])
            if minimum != 0:
                output.extend([key] * minimum)
        return output