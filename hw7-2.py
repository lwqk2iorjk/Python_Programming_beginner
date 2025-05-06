def to_minutes(hours, minutes):
    return hours * 60 + minutes

a = int(input("請輸入小時："))
b = int(input("請輸入分鐘："))

x = to_minutes(a, b)
print("總共為", x, "分鐘")
