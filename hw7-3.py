def rectangle_area(width, height):
    return width * height

width = float(input("請輸入矩形的寬："))
height = float(input("請輸入矩形的高："))

area = rectangle_area(width, height)
print("矩形面積為：", area)
