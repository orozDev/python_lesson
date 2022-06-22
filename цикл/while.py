n = int(input('Введите число для вычисления: '))
i = 0
s = 0
while True:
    i += 1
    s += i
    if i >= n:
        break
    else:
        continue

print(s)