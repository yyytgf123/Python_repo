n = int(input())

room = 1
cnt = 1

# 벌집 개수가 주위로 6 -> 12 -> 18 -> 24개씩 증가
# 그래서 1칸 옆에는 중심 1 + 6인 7까지이고 2칸 옆은 8부터 19까지, 구조
# while문 한 번 돌 때마다 한 칸씩 이동하여 cnt 증가와 주위 1칸씩 증가
# 주위 한 칸씩 증가는 이동 수(cnt) * 6으로 해줌

while n > room:
    room += 6 * cnt
    cnt += 1

print(cnt)