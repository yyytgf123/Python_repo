N = int(input())
group_word = N

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        # j부터 j+1씩하여 똑같은 문자인지 확인
        # 같은 문자이면 계속 continue하여 다음 for문 동작
        # 다르면 elif
        if word[j] == word[j+1]:
            continue
        # j부터 j+1부터 마지막 글자까지 j의 문자가 있으면 -1함
        # 즉 해당 문장은 연속적이지 않다고 판단 -1해줌
        # 이후 break하여 다음 for문 동작
        elif word[j] in word[j+1:]:
            group_word -= 1
            break

print(group_word)