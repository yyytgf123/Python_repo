chess = [1,1,2,2,2,8]

user_input = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - user_input[i], end=' ')