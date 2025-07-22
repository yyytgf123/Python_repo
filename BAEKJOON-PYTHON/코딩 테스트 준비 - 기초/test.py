arr = []
arr_len = []
ans = ''

for i in range(5):
    user_input = input().split()
    arr.append(user_input)
    arr_len.append(len(user_input))

for i in range(max(arr_len)):
    for j in range(5):
        
        print(arr_len[j])
        print(arr[j])

        if i < arr_len[j]:
            ans += (arr[j][i])

print(ans)
