class Questions():
    question = ''
    answers = []
    right_answer = 0

    def __init__(self, question, answers, right_answer):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

class Quiz():
    title = ''
    questions = []

    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def start_quiz(self):
        count = 0
        print(f'\n    Виктарина "{self.title}" началось')
        for question in self.questions:
            print(f'{question.question}\n')
            for answer in question.answers:
                idx = question.answers.index(answer)
                print(f'{idx}: {answer}')
            temp = int(input('\nВведите вариант: '))
            if temp == question.right_answer:
                count += 1 
        print(f'\nВаш балл составляет {count}')
    


fist_task = Questions(
    '\nКто изабрель python ?',
    ['Гвидо Ван Рассум', 'Кто-то', 'Не знаю'],
    0,
)

second_task = Questions(
    'Кто открыл компанию Google ?',
    ['Сергей', 'Сергей брин и Лари Пейтж', 'Random name', 'Марк Цукеберг'],
    1,    
)

def select_quiz(quizs):
    for i in range(len(quizs)):
        print(f'{i}: {quizs[i].title}')
    n = int(input('\nВведите порядковый номер викторины: '))
    if n - 1 > len(quizs) or n < 0:
        print(f'\n{n}-го викторины не существует')
    else:
        quiz = quizs[n]
        quiz.start_quiz()


quiz = Quiz(
    'Известные люди',
    [fist_task, second_task],
)

quizs = [quiz]

while True:
    print(
        '\nВыберитке пункт',
        '\n1: Начать виктарину',
        '\n2: Добавить виктарину',        
    )

    n = int(input('\nВведите порядковый номер пункта: '))

    if n == 1:
        select_quiz(quizs)
    elif n == 2:
        pass
    else:
        print('Досвидание')
        break