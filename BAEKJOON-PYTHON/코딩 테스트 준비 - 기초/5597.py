stu = []
n_stu = []

for i in range(28):
    num = int(input())
    stu.append(num)

for i in range(1,31):
    # i를 1부터 30까지 받아서 stu 배열의 값과 하나씩 비교
    # 없으면 n_stu에 추가
    # 문자형도 가능
    if i not in stu:
        n_stu.append(i)

print(min(n_stu))
print(max(n_stu))