loop = int(input())
store = []
count = 0

for i in range(loop):
    user_input = input()
    print(len(user_input))
    for j in len(user_input):
        if store not in user_input:
            store.append(j)
            count += 1
        
print(count)