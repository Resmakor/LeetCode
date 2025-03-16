class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        even_digits = [x for x in digits if x % 2 == 0]
        if len(even_digits) == 0:
            return 0
        valid_numbers = set()
        for perm in permutations(digits, 3):
            number = ''.join(str(perm))
            if perm[2] % 2 == 0 and perm[0] != 0:
                valid_numbers.add(number)
        return len(valid_numbers)
                    
    
