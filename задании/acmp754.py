def is_valid(n):
    if n > 93 and n < 728:
        return True
    return False

a, b, c = map(int, input().split())

if is_valid(a) and is_valid(b) and is_valid(c): 
    max(a, b, c)
else:
    print('Error')