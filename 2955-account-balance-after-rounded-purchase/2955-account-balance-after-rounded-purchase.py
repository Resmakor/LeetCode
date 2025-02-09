class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        modulo = purchaseAmount % 10
        if modulo >= 5:
            return 100 - (purchaseAmount + (10 - modulo))
        return 100 - (purchaseAmount - modulo)