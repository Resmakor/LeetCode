class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for account in accounts:
            account_wealth = sum(account)
            if account_wealth > richest:
                richest = account_wealth
        return richest
        