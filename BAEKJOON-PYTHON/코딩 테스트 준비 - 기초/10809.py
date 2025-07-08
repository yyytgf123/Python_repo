s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

# print(s.index("a")) -> 2
# => 해당 문자열에 해당하는 문자의 index를 출력

for i in alpha:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')