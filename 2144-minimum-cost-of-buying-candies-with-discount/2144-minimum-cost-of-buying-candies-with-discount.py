class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_size = len(cost)
        if cost_size <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        output = 0
        for i in range(0, cost_size, 3):
            if i + 1 < cost_size:
                output += cost[i] + cost[i + 1]
            else:
                output += cost[i]
        return output