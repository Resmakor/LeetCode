class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        given_candies = [0] * num_people
        giving_amount = 1
        while candies != 0:
            for i in range(num_people):
                if candies - giving_amount > 0:
                    given_candies[i] += giving_amount
                    candies -= giving_amount
                elif candies - giving_amount <= 0:
                    given_candies[i] += candies
                    return given_candies
                giving_amount += 1 
        return given_candies