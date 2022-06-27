# a = int(input('1: '))
# b = int(input('2: '))

# def is_check(n, index):
#     if n % 2 == 0:
#         return str(index) + ' is even'
#     else:
#         return str(index) + ' is odd'

# a = is_check(a, 'fist number')

# print(a)
import math
number = int(input(':'))
lst = []
def square(n):
    p = n * 4
    lst.append('perimetr')
    lst.append(p)

    pl = n ** 2
    lst.append('ploshad')
    lst.append(pl)

    # di = n * math.sqrt(n)
    di = ((2*n**2)**.5)

    lst.append('diagonal')
    lst.append(di)
    print(lst)

function = square(number)
print(function)


