s = input().split()
count = 0

for i in range(len(s)):
    for j in s[i]:
        # j가 ABC에 포함만 되어있으면됌
        # j = A, B, C, AB, BC, ABC 다 가능
        if j in "ABC":
            count += 3
        elif j in "DEF":
            count += 4
        elif j in "GHI":
            count += 5
        elif j in "JKL":
            count += 6
        elif j in "MNO":
            count += 7
        elif j in "PQRS":
            count += 8
        elif j in "TUV":
            count += 9
        elif j in "WXYZ":
            count += 10

print(count)
