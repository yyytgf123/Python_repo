import sys

count = int(sys.stdin.readline())

for _ in range(count) :
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)