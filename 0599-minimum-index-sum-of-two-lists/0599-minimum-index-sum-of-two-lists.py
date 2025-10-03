class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common_strings = set(list1).intersection(set(list2)) 
        hashMap1 = defaultdict(list)
        hashMap2 = defaultdict(list)
        for index, element in enumerate(list1):
            hashMap1[element] = index
        for index, element in enumerate(list2):
            hashMap2[element] = index
        least_sum = max(hashMap1.values()) + max(hashMap2.values())
        output = []
        for string in common_strings:
            curr_sum = hashMap1[string] + hashMap2[string]
            if curr_sum < least_sum:
                least_sum = curr_sum
        for string in common_strings:
            if hashMap1[string] + hashMap2[string] == least_sum:
                output.append(string)
        return output