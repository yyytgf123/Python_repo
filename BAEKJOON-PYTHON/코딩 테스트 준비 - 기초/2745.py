num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x , b = map(str, input().split())
x = x[::-1]
result = 0

# ZZZZZ 36 입력 시
# num.index() = 35
# int(b)**i = 36**i
for i in range(len(x)):
    result += (int(b)**i)*(num.index(x[i]))

print(result)