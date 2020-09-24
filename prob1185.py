class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        def computeDays(target, s_year):
            days = 0
            for year in range(s_year, target['year']):
                days += 366 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 365
            for day in months[:target['month']-1]:
                days += day
            days += target['day']+1 if target['month'] >= 3 and (target['year'] % 4 == 0 and target['year'] % 100 != 0 or target['year'] % 400 == 0) else target['day']
            return days
            
        s_year = min(year, 2020)
        day1 = {'year': 2020, 'month': 9, 'day': 19}
        day2 = {'year': year, 'month': month, 'day': day}
        day1 = computeDays(day1, s_year)
        day2 = computeDays(day2, s_year)
        return weekdays[ (day2 - day1) % 7]
        
        # 2019/09/14 is Saturday
        # 計算兩個日期分別到 較小年份的一月一號 是差幾天
        # 再使用這兩個天數的差來算星期
        # 例如目標為 2022/7/23，計算
        # 2020/1/1 ~ 2022/7/23 有 935 天
        # 2020/1/1 ~ 2020/9/19 有 263 天
        # (965-263) % 7 == 0
