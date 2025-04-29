def convert_year(year):
    if year >= 1911:
        print("西元", year, "年 是民國", year - 1911, "年")
    elif year >= 1:
        print("民國", year, "年 是西元", year + 1911, "年")
    else:
        print("請輸入正確的年份")

year = int(input("請輸入民國或西元年份："))
convert_year(year)
