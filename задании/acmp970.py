a, b, c = map(int, input().split())

if a + b == c or a - b == c:
    print("YES")
elif b + c == a or b - c == a:
    print("YES")
elif a + c == b or a - c == b:
    print("YES")
else:
    print("NO")