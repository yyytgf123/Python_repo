n = int(input())
socre = list(map(int, input().split()))
max_M = max(socre)

avg = []
for i in socre:
    avg.append(i/max_M*100)

total_avg = sum(avg)/n
print(total_avg) 