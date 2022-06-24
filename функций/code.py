a = int(input('1: '))
b = int(input('2: '))

def is_check(n, index):
    if n % 2 == 0:
        return str(index) + ' is even'
    else:
        return str(index) + ' is odd'

a = is_check(a, 'fist number')

print(a)


