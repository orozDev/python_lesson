class Phone():
    title = ''
    ram = '3gb'
    size_of_battery = ''
    front_camera = ''
    main_camera = ''
    storage = ''
    type_of_display = ''


redmi = Phone()
redmi.title = 'Xiaomi Redmi Note 9'
redmi.size_of_battery = '5020mH'
redmi.front_camera = '15px'
redmi.main_camera = '48px'
redmi.storage = '64gb'
redmi.type_of_display = 'IPS'

samsung = Phone()
samsung.title = 'Samsung galaxy A8'
samsung.size_of_battery = '4000mH'
samsung.front_camera = '15px'
samsung.main_camera = '48px'
samsung.storage = '64gb'
samsung.type_of_display = 'Amoled'

print(redmi.title)
print(samsung.ram)