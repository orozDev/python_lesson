# ______1__
#n = int(input())
#array = list(map(int, input().split(' ')))
# print(min(array), max(array))


#_______2__
# n = int(input())
# array = list(map(int, input().split(' ')))
# mx = array[0]
# mn = array[0]

# for i in range(len(array)):
#     if mx < array[i]:
#         mx = array[i]
#     if mn > array[i]:
#         mn = array[i]
# print(mn, mx)


#_______3__
n = int(input())
array = list(map(int, input().split(' ')))
maximum = array[0]
minimum = array[0]

for i in array:
    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i
  
print(minimum, maximum)

