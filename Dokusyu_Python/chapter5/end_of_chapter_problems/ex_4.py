import datetime
import locale
import calendar

# 1
str1 = 'となりのきゃくはよくきゃきくくうきゃくだ'
print(str1.rfind('きゃく'))

# 2
print('{}の気温は{:.2f}℃です。'.format('千葉', 17.256))

# 3
str2 = '彼女の名前は花子です。'
str2 = str2.replace('彼女', '妻')
print(str2)

# 4
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
dt = datetime.datetime.today()
dt_p = dt + datetime.timedelta(days=5, hours=6)
print(dt_p)

# 5
calendar.setfirstweekday(6)
print(calendar.month(2020, 10, 5))