# 첫 번쨰 풀이, 인덱스가 없으면 에러 발생
# arr = []

# for i in range(5):
#     A = list(map(str, input().split()))
#     arr.append(A)

# print(arr)

# for i in range(6):
#     for j in range(5):
#         print(arr[j][i], end= "")


# 정답, 최대 인덱스의 길이를 
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
            ans+=lines[i][j]

print(ans)

## 설명
# j가 최대 길이까지 순회, i는 배열의 열을 반복
# 그래서 0부터 최대 길이까지 1씩 증가할때마다 1열부터 5열까지
# j의 현재 길이보다 열의 행의 길이가 더 길면 현재 i의 열과 j의 행의 인덱스 값을
# ans에 추가해주고 아닌 경우 pass
# 결론 : 최대 인덱스 길이를 이용하여 최대 인덱스 길이보다 짧은 열의 행을 가져도
#        if문으로 그냥 pass가 되어 위와 같이 공백이 생겨도 문제가 발생하지 않음