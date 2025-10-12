import re
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        output = set()
        numbers = list(set(re.split('[a-z]', word)))
        print(numbers)
        for num in numbers:
            if num == '':
                continue
            elif num == '0':
                output.add(num)
            elif num.count('0') == len(num) and len(num) > 1:
                output.add('0')
            else:
                output.add(num.lstrip('0'))
        return len(output)