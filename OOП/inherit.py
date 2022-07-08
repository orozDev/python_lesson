class Doctor():
    title = ''

    def __init__(self, title):
        self.title = title

    def sayHello(self):
        print('Hello, Im a doctor')


class Police():
    status = ''

    def __init__(self, status):
        self.status = status

    def sayHello(self):
        print('Hello, Im a police')


class Person(Police, Doctor,):
    name = ''
    age = 0
    phone_number = ''
    address = ''

    def __init__(self, name, age, phone_number, address, title, status):
        super().__init__(status)
        Doctor.__init__(self, title)
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.address = address

person = Person(
    'Alex',
    12,
    '12121212121212',
    '12 st. Osh Kyrg',
    'Okoolist',
    'sergeant',
)


person.sayHello()


# class A(object):
#     def __init__(self):
#         print("Entering A")
#         print("Leaving A")

# class B(object):
#     def __init__(self):
#         print("Entering B")
#         super(B, self).__init__()
#         print("Leaving B")

# class C(A, B):
#     def __init__(self):
#         print("Entering C")
#         super(C, self).__init__()
#         print("Leaving C")