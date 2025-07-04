# n : 바구니 수, m : 공을 넣는 수
n, m = map(int, input().split())
# 공이 없으면 0이니 0으로 초기화
basket = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        basket[index - 1] = k

for i in range(n):
    print(basket[i, end=" "])