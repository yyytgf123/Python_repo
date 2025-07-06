N, M = map(int, input().split())

# 0번째 인덱스부터 1 ~ N까지 값이 삽입
bucket = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    
    temp = bucket[i - 1]
    bucket[i - 1] = bucket[j - 1]
    bucket[j - 1] = temp

# 0부터 N - 1의 인덱스까지 출력
for j in range(N):
    print(bucket[j], end = ' ')