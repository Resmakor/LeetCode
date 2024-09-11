class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        max_index = 0
        for element in nums1 + nums2:
            if element[0] > max_index:
                max_index = element[0]
        for i in range(max_index):
            temp_list = []
            for element in nums1:
                if element[0] == i + 1:
                    temp_list = [i + 1, element[1]]
            for element in nums2:
                if element[0] == i + 1:
                    if not temp_list:
                        temp_list = temp_list = [i + 1, element[1]]
                    else:
                        temp_list = [i + 1, temp_list[1] + element[1]]
            if temp_list:
                output.append(temp_list)
        return output