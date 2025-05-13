grades = []

for i in range(5):
    score = float(input(f"請輸入第 {i+1} 位學生的成績："))
    grades.append(score)

average = sum(grades) / len(grades)
print("平均成績為：", average)
