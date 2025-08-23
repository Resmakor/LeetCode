class Solution:
    def reformatDate(self, date: str) -> str:
        out_day, out_month = "", ""
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        out_day = ""
        if day[1] < '0' or day[1] > '9':
            out_day = '0' + day[0]
        else:
            out_day = day[0] + day[1]
        out_month = str(months.index(month) + 1)
        if len(out_month) == 1:
            out_month = '0' + out_month
        return f"{year}-{out_month}-{out_day}"    
        