class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_nums = {}
        output = []
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    dict_nums[nums2[i]] = nums2[j]
                    break
            if nums2[i] not in dict_nums.keys():
                dict_nums[nums2[i]] = -1
        for element in nums1:
            output.append(dict_nums[element])
        return output