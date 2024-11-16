class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        numbers = []
        for word in s.split():
            current_number = ""
            for letter in word:
                if letter < '0' or letter > '9':
                    current_number = ""
                    break
                else:
                    current_number += letter
            if current_number != "":
                numbers.append(current_number)  
        numbers = [int(element) for element in numbers]
        for i in range(len(numbers) - 1):
            if numbers[i] >= numbers[i + 1]:
                return False
        return True