total = 0

for i in range(10):
    num = float(input(f"請輸入第 {i+1} 個數："))
    total += num

average = total / 10
print("平均值為：", average)
