money  = int(input('Сколько у вас денег: '))

lagman = 150
manty = 200
sum = lagman + manty

if money < 200 and money >= lagman:
    print('Вы можеть купить логман, но на манты не хватит денег')
elif sum > money and money >= manty:
     print('Вы можеть купить манты или логман')
elif money >= sum:
    print('Вы можеть позволить себе логман и манты')
else:
    print('У вас недостаточно денег на пропитания')

# == проверка на равенство 
# != проверка на неравенство
# >= больше или равно
# <= меньше или равно
# > больше чем ...
# < меньше чем ...