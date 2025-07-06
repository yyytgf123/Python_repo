arr = []
for i in range(10):
    a  = int(input())
    # a를 42로 나눠서 arr에 없으면 arr에 추가
    # 그래서 안겹쳐지는 나머지 수는 배열에 계속 추가되어 서로 다른 값이 몇 개인지 파악
    if a%42 not in arr:
        arr.append(a % 42)

print(len(arr))