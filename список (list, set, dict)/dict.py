students = [
    {
        'name': 'Gulzina',
        'group': 'FullStack',
        'phone_number': '0557 04 70 02',
    },
    {
        'name': 'Kutman',
        'group': 'FullStack',
        'phone_number': '0508 21 67 57',
    },
    {
        'name': 'Ruslan',
        'group': 'FullStack',
        'phone_number': '0508 21 67 57',
    },
    {
        'name': 'Almagul',
        'group': 'FullStack',
        'phone_number': '0508 21 67 57',
    },
]

temp = {
    'name': 'Oroz',
    'group': 'FullStack',
    'phone_number': '0776 780 472',
}

temp['age'] = 18

print(temp['age'])

students.append(temp)
size = len(students) - 1
print(students[size])

print(students[1]['name'][3:len(students[1]['name'])])

