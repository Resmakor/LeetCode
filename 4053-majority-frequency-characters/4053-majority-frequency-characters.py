class Solution(object):
    def majorityFrequencyGroup(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        d = defaultdict(list)
        for key in counter:
            d[counter[key]].append(key)
        curr_group_size = 0
        output = ""
        for key in d:
            if len(d[key]) >= curr_group_size:
                output = d[key]
                curr_group_size = len(d[key])
        return ''.join(output)