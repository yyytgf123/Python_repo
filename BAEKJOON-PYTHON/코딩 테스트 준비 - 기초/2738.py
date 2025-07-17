# 직접짠 코드 -> valueError
# N, M = map(int,input().split())

# array = [[0]*N for _ in range(M*2)]
# array2 = [[0]*N for _ in range(M*2)]

# for a in range(M):
#     i, j, k = map(int,input().split())
#     array[a] = i, j, k

# for a in range(M):
#     i, j, k = map(int,input().split())
#     array2[a] = i, j, k

# for i in range(N):
#     for j in range(M):
#         print(array[i][j] + array2[i][j], end=" ")
#     print()

# 수정
N, M = map(int, input().split())

array = []
array2 = []

for _ in range(N):
    array.append(list(map(int, input().split())))

for _ in range(N):
    array2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(array[i][j] + array2[i][j], end=" ")
    print()