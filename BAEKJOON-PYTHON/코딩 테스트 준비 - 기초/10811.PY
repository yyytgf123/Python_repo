N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]


for i in range(M):
    i, j = map(int, input().split())
    # i가 1부터 5인 경우
    # arr[0] ~ arr[4] 까지 받아와서 reverse
    temp = arr[i-1 : j]
    arr[i-1:j] = temp[::-1]

for i in range(len(arr)):
    print(arr[i], end= ' ')