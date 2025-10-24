class Solution(object):
    def __init__(self):
        self.allowed = ["electronics", "grocery", "pharmacy", "restaurant"]
        self.allowed_set = set(self.allowed)
    def is_valid(self, coupon, active, line):
        if not active or not coupon or line not in self.allowed_set:
            return False
        for letter in coupon:
            if not (letter.isalnum() or letter == '_'):
                return False
        return True
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        output, valid = [], []
        for i in range(len(code)):
            if self.is_valid(code[i], isActive[i], businessLine[i]):
                valid.append([code[i], businessLine[i]])
        for category in self.allowed:
            temp = []
            for pair in valid:
                if pair[1] == category:
                    temp.append(pair[0])
            temp.sort()
            output.extend(temp)
        return output