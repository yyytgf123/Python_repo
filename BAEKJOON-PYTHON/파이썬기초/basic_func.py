### 입력 ###
temp = input()

temp = int(input)

temp = float(input)

# int형 입력 값 여러 개
a, b, bb = map(int, input().split())
print(a, b, bb)

# str형 입력 값 여러 개
c, d = map(str, input().split())

# int형 리스트 형태로 저장
e = list(map(int, input().split()))
print(e)

# int형 2차원 배열 형태로 저장
f = [list(map(int, input().split())) for _ in range(10)]
print(f)

### 출력 ###
print("hello world!")

# 특수 문자 출력 \뒤에 입력
print("\"hello world\"")

# 소수점 2번째까지 출력
temp = float(input())
print("%.2f" %temp)

# 값을 5칸으로 출력, 즉 앞에 공백 4개 생성
second = 5
print("%5d" %second)

# for문으로 temp2 값을 반복 출력하는데 end=" "으로 마지막마다 공백 추가
temp2 = [1,2,3,4,5]
print(temp)
for i in temp2 :
    print(i, end=" ")

# 2차원 리스트 출력
temp3 = [[1,2,3,4,5], [6,7,8,9,0]]
for i in temp3 :
    for j in i :
        print(j, end= " ")
    print()

### 리스트 ###
# 1차원 리스트 생성
temp = [0 for _ in range(10)]
print(temp)

# 2차원 리스트 생성
temp = [[0 for _ in range(10)] for j in range(10)]
print(temp)

# list 자리를 출력
temp = [1,2,3,4,5]
for i in range(len(temp)) :
    print(i, end=" ")

# 2차원 리스트 자리를 출력
temp = [[1,2,3,4,5],[6,7,8,9,0]]
for i in range(len(temp)) :
    for j in range(len(temp[i])) :
        print("%d,%d"%(i, j), end=" ")
    print()