## 풀이 1
N = int(input())
L = list(map(int, input().split()))
V = int(input())
print(L.count(V))

## 풀이 2, N,L,V에서 추가
count = 0
for i in L:
    if i == V:
        count += 1
    
print(count)