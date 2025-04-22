year = int(input("請輸入年份："))
month = int(input("請輸入月份："))

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("此月份有29天")
    else:
        print("此月份有28天")
elif month in [4, 6, 9, 11]:
    print("此月份有30天")
else:
    print("此月份有31天")
