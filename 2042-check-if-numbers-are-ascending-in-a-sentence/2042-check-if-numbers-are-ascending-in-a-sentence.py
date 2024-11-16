class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numbers = []
        s = s.split()
        for word in s:
            current_number = ""
            for letter in word:
                if letter < '0' or letter > '9':
                    current_number = ""
                    break
                else:
                    current_number += letter
            if current_number != "":
                numbers.append(current_number)  
        for i in range(len(numbers) - 1):
            if int(numbers[i]) >= int(numbers[i + 1]):
                return False
        return True