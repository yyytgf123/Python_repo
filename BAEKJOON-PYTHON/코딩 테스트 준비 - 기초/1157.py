word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    # input값 - ZZZXX 가정
    # max(cnt) = 3
    # cnt.index(3) = 0 - 숫자 3의 인덱스 위치를 구함
    # word_list[0] = Z - 0번째 인덱스의 문자
    print(word_list[(cnt.index(max(cnt)))])

# 정리
# 이 문제에서 핵심은 word_list와 cnt를 사용해서 word_list로 중복을 없앤
# 문자들이 나오는 수를 cnt에 추가해서 문자별 나오는 수를 저장하고 
# 제일 많이 나오는 값을 출력