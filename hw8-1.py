positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input(f"請輸入第 {i+1} 個整數："))
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("正數個數：", positive)
print("負數個數：", negative)
print("零的個數：", zero)
