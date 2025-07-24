quarter = 25
dime = 10
nickel = 5
penny = 1

sum = []

user_input = int(input())

for _ in range(user_input):
    change = int(input())
    A = change // quarter
    B = (change - (A * quarter)) // dime
    C = (change - (A * quarter + B * dime)) // nickel
    D = (change - (A * quarter + B * dime + C * nickel)) // penny
    
    print(A, B, C, D)