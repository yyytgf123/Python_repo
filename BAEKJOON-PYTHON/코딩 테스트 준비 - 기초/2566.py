a = []

for i in range(9):
        a.append(list(map(int, input().split())))

max_value = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
          if a[i][j] >= max_value:
                max_value = a[i][j]
                row = i+1
                col = j+1

print(max_value)
print(row, col)