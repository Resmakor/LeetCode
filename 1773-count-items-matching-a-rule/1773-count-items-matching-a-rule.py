class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        output = 0
        if ruleKey == 'type':
            index = 0
        elif ruleKey == 'color':
            index = 1
        elif ruleKey == 'name':
            index = 2 
        for item in items:
            if ruleValue == item[index]:
                output += 1
        return output