class User():
    def __init__(self, name, age, email, username, password):
        self.name = name
        self.age = age
        self.email = email
        self.username = username
        self.__password = password

    def get_data(self):
        print('\n', self.__dict__)

    def logout(self):
        return True
  
    def set_password(password, new_password):
        if password == User.__password:
            User.__password = new_password
            print('\nПароль успешно изменен!\n')
        else: 
            print('\nНеверный пароль!\n')

    def get_password():
        return User.__password
    
name = input('Ваше имя: ')
age = input('Ваш возраст: ')
email = input('Ваша почта: ')
username = input('Логин: ')
password = input('Придумайте пароль: ')

user = User(name, age, email, username, password)

print('Регистрация прошла успешно!\n')
print(user.get_password())
print('Авторизция!') 
is_authenticated = False
username = input('Логин: ')
password = input('Введите пароль: ')

if username == user.username:
    if password == user.get_password():
        is_authenticated = True
    else:
        print('Неверный пароль!')
else:
    print('не существует пользователя!')

if is_authenticated:
    while True:
        print('\nВыберите функцию:')
        print('1: Получить Персональные данные')
        print('2: Получить пароль')
        print('3: Изменить пароль')
        print('4: Выход\n')

        n = int(input('Введите цифру: '))

        if n == 1:
            user.get_data()
        elif n == 2:
            user.get_password()
        elif n == 3:
            password = input('Введите старый пароль: ')
            new_password = input('Введите новый пароль: ')
            user.set_password(password, new_password)
        elif n == 4:
            if user.logout():
                print('Вы вышли из аккаунта! Досвидание!')
                is_authenticated = False
                break
        else:
            continue


    

