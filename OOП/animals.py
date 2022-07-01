class Animals():
    title = ''
    color = ''
    food = ''
    type = ''
    def __init__(self, title, color, food, type, height=None):
        self.title = title
        self.color = color
        self.food = food
        self.type = type
        if height != None:
            self.height = height

    def run(self):
        print('Ат жүгүрүп жатат')

    def sounds(self):
        print('ий - го - го!!')
        print(self.title)
    
    def turn(self, side=None, amount=1):
        print(f'{self.title} бурулду {side} {amount} жолу')


hourse = Animals('Ат', 'ак', 'чөп', 'пони', height='100cm')
hourse.age = 3
hourse.run()
hourse.sounds()
hourse.turn(amount=4, side='солго')

print(hourse.age)