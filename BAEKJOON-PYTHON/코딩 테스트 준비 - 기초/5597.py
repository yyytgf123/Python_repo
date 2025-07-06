stu = []
n_stu = []

for i in range(28):
    num = int(input())
    stu.append(num)

for i in range(1,31):
    if i not in stu:
        n_stu.append(i)

print(min(n_stu))
print(max(n_stu))