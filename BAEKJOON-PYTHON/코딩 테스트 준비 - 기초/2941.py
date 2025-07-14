user_input = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    user_input = user_input.replace(i, "*")

print(len(user_input))