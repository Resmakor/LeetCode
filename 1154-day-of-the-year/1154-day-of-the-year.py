import datetime
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        curr_day = int(date[8:])
        month = int(date[5:7])
        year = int(date[0:4])
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        if is_leap_year:
            days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days[0:month - 1]) + curr_day
        