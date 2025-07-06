# n : 바구니 수, m : 공을 넣는 수
n, m = map(int, input().split())
# 공이 없으면 0이니 0으로 초기화
basket = [0] * n

for _ in range(m):
    # i번 부터 j번까지, j + 1은 range는 마지막 값은 포함하지 않음
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        # 실제 인덱스는 0번부터 시작하니 1번이 index[0]이여서 -1
        basket[index - 1] = k

for i in range(n):
    print(basket[i], end=" ")