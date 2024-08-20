class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequencies = dict()
        for element in nums:
            if element not in frequencies.keys():
                frequencies[element] = 1
            else:
                frequencies[element] += 1
        sorted_freq = sorted(frequencies.items(), key=lambda x:x[1])
        
        for j in range(len(sorted_freq) - 1):
            flag = True
            for i in range(len(sorted_freq) - 1):
                if sorted_freq[i][1] == sorted_freq[i + 1][1] and sorted_freq[i][0] < sorted_freq[i + 1][0]:
                    sorted_freq[i], sorted_freq[i + 1] = sorted_freq[i + 1], sorted_freq[i]
                    flag = False
            if flag == True:
                break
        output = []
        for element in sorted_freq:
            output.extend([element[0]] * element[1])
        return output
        #sub_li.sort(key = lambda x: x[1])