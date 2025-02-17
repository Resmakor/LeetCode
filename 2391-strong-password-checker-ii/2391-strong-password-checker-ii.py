class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        lowercase, uppercase, digit, special_char = False, False, False, False
        for i, char in enumerate(password):
            if char >= 'a' and char <= 'z':
                lowercase = True
            elif char >= 'A' and char <= 'Z':
                uppercase = True
            elif char >= '0' and char <= '9':
                digit = True
            else:
                special_char = True
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        return lowercase and uppercase and digit and special_char