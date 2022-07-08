class Procduct():
    title = ''
    price = 0.0
    made_place = ''
    company = ''
    description = ''

    def __init__(self, title, price, made_place, company, description):
        self.title = title
        self.price = price
        self.made_place = made_place
        self.company = company
        self.description = description
    
    def getPrice(self):
        return f'{self.price} $'


class Smartphone(Procduct):
    storage = 0
    ram = 0
    prosessor = ''
    main_camera = 0
    front_camera = 0
    battery = 0

    def getInfo(self):
        super().getPrice()
        print(self.__dict__)

class Car(Procduct):
    motor = ''
    color = ''
    year = 0

    def __init__(
        self, 
        title, 
        price, 
        made_place, 
        company, 
        description,
        motor,
        color,
        year,
    ):
        super().__init__(title, price, made_place, company, description)
        self.motor = motor
        self.color = color
        self.year = year
        
    def getMotorAndPrice(self):
        print(f'{self.motor} - {super().getPrice()}')


nissan = Car(
    'Nissan GTR r34',
    50000,
    'Japan',
    'Nissan',
    'this car is japanese',
    'gtr turbo r34',
    'blue',
    2000,
)
nissan.getMotorAndPrice()
print(nissan.__dict__)