values = []
counter = 0
n = input()
for i in list(n):
    if i == '0':
        counter += 1
    else:
        values.append(counter)
        counter = 0

print(max(values))