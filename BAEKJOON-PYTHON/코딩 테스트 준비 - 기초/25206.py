# 딕셔너리를 사용하여 문제 해결
score = {'A+': 4.5, 'A0':4.0, 'B+':3.5,
            'B0': 3.0, 'C+':2.5, 'C0':2.0,
            'D+':1.5, 'D0':1.0, 'F':0.0}
average = 0
total = 0

for i in range(20):
    lecture, credit, grade = input().split()
    if grade == 'P':
        continue
    else:
        # 점수 : 학점 수 x 등급
        average += float(credit)*score[grade]
        total += float(credit)

# 평균 : 점수 / 총 듣는 학점 수
print(average/total)