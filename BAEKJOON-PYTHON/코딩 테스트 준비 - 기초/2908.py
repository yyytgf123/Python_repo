num1, num2 = input().split()
# [::-1]은 str형만 되어서 num1,num2를 str로 받고 뒤집은 뒤 int형으로 변환
a = int(num1[::-1])
b = int(num2[::-1])

if a > b:
    print(a)
else:
    print(b)
