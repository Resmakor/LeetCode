class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        output = 0
        for i in range(low, high + 1, 1):
            i_str = str(i)
            i_str_len = len(i_str)
            print(i)
            if i_str_len % 2 == 0:
                n = i_str_len // 2
                first_part = sum([int(x) for x in list(i_str[0:n])])
                second_part = sum([int(x) for x in list(i_str[n:])])
                if first_part == second_part:
                    output += 1
        return output