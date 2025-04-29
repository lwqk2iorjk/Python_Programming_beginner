score = int(input("請輸入成績："))

if score < 0 or score > 100:
    print("請輸入0到100之間的成績")
elif 90 <= score <= 100:
    print("A等")
elif 80 <= score < 90:
    print("B等")
elif 70 <= score < 80:
    print("C等")
elif 60 <= score < 70:
    print("D等")
else:
    print("E等")
