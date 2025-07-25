A, B, V = list(map(int, input().split()))
days = (V - B - 1) // (A - B) + 1
print(days)
# A B V
# 2 1 5

# (5 - 1 -1) // (2 - 1) + 1

# 3 // 2 