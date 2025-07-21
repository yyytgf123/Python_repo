# 첫 번쨰 풀이
# arr = []

# for i in range(5):
#     A = list(map(str, input().split()))
#     arr.append(A)

# print(arr)

# for i in range(6):
#     for j in range(5):
#         print(arr[j][i], end= "")

lines= []
length = [] 
ans = ''
for _ in range(5):
    line=input()
    length.append(len(line))
    lines.append(line)

print(length)
print(lines)

for j in range(max(length)):
    for i in range(5):
        if j< length[i]:
            print(lines[i][j])
            ans+=lines[i][j]

print(ans)