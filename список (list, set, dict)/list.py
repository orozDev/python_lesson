# a = [13434, 222, 3433, 454 , 3455, 546]
# b = a[4] + 2
# a[4] = 2
# print(a[4])

# length = len(a)
# print(type(length))

students = [
    'Gulzina-Gulzina', 
    'Almagul', 
    'Kutman', 
    'Ruslan',
    'Oroz',
]
# f = "😇"
# total = f.join(students)
# print(total)

# name = students[0]

# print(name.split('-'))

# n = input()

# array = n.split(' ')

# print(array)
# int()
# str()
# bool()
# float()
# list()
# dict()
# set()

# students2 = [
#     'Mike',
#     'John',
#     'Mary',
#     'John'
# ]

# students2.append('Meerim')
# students2.insert(1, 'Medina')
# students2.remove('John')
# students2.pop(3)
# students2.extend(students)

# print(students2)


array2 = list('or')

print(array2)

# DICTIONARY 

dict1 = {} #empty
          # key    value
# dict1 = {'name':'Alex',1:'Age',2:'surename'} 1 

# dict1 = dict([('name','age'),('tom','20')]) 2

# dict1 = dict.fromkeys(['a','b'], 10) 3

dict1 = {a: a ** 2 for a in range(7)}
dict2 = {}
for item in range(7):
    dict2[item] = item * 2

# print(dict1)
# print(dict2)

dict3 = {1:'a',2:'b',3:'c',4:'d'}
# print(dict3)
# dict3[3] = 'three'
# print(dict3)

# for item in dict3:
#     print(dict3[item])

dict4 = {'brendoflaptop':['acer','asus','mac'],
'brendogphone':['sumsung','miu','poco','nokia3310','iphone'],
'markofcar':['subaru','mark','nissan','mustank','tiko'],
1:['hdsgfhgdjf']}
# print(dict4['brendoflaptop'][2])
# dict3.clear() # очишает список 
# d = dict4.copy() # копия словаря
# d2  = dict4
# print(dict4.get(['brendoflaptop']))
# dict4.pop(1) # удалет по индексу
#print(dict4.values()) # возвращает значание словаря
# print(d2
# print('--------------------------')
# print(dict4)
# print(type(dict4))

# tuple
dag = ('d','a','g')
# tuple = ()
# print(type(tuple))
# print(dag)
# mix = ('c',0,[1,2,3],True,{'name':'Luis'})
# for item in mix:
#     print(item,':',type(item))

g = []
tuple = ('lagman','pelpeni','indiyski chay',"let's go")
# print(tuple)
# tuple = 1,2,3,4,5,6,7
# tuple.append('lambarginy')
# print(tuple[2])

words = {'cat':'koshka','dog':'sabaka','bird':'ptichka'}

work = int(input('начать%отмена 1 или 0:'))
while work == 1:
    word = input('Введите слово которое нужно перевести:')
    for i in words:
        if i == word:
            print(word,'translate:',words[i] )
    work = 0
    # work = int(input('продолжить%закончить 1 или 0:'))
