import datetime
import calendar
m, d, y = map(int, input().split())
input_data = datetime.date(y, m, d)
print(calendar.day_name[input_data.weekday()].upper())