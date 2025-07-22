from sys import stdin

input = stdin.readline

n = int(input())
# 100 x 100 배열, 0으로 초기화
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    # a를 height, b를 width로 받음
    # 높이(a)당 길이(b)를 1로 채움
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

res = 0
# 모두 더함
for i in arr:
    res += sum(i)

print(res)