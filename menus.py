import event

def start_menu(): #Стартовое меню
    IF = 0
    while IF == 0:
        print("Введи 0, чтобы открыть профиль")
        print("Введи 1, чтобы выйти в город")
        answer = int(input())
        if answer == 0:
            IF = 1
            profile()
        elif answer == 1:
            IF = 1
            start_city()
        else:
            print("Неверное значение")

def profile(): #Профиль
    IF = 0
    print("Профиль игрока:", name)
    print("Уровень:", lvl)
    print("Опыт:", exp, "/", max_exp)
    print("Здоровье:", health)
    print("Золото", gold)
    print("Урон:", damage)
    print("Защита", defense)
    print("Скорость:", speed)
    while IF == 0:
        print("Введи 1, чтобы вернуться назад")
        print("Введи 2, чтобы открыть инвентарь")
        print("Введи 3, чтобы сменить имя")
        answer = int(input())
        if answer == 1:
            IF = 1
            event.back_to()
        elif answer == 2:
            pos = 1
            IF = 1
            menus.inventory()
        elif answer == 3:
            event.change_name
        else:
            print("Неверное значение")

def inventory(): #Инвентарь
    print("Системы нвентаря пока, что нету, так что вернись обратно")
    time.sleep(1)
    profile()
    pos = 0
    
def start_city(): #Стартовый город
    IF = 0
    print("Введи 1, чтобы закупиться провиантом")
    print("Введи 2, чтобы купить снаряжение")
    print("Введи 3, чтобы прокачаться в кузнице")
    print("Введи 0, чтобы открыть профиль")
    while IF == 0:
        if answer == 1:
            pos = 2
            IF = 1
            menus.start_food_shop()
        elif answer == 2:
            pos = 2
            IF = 1
            menus.start_equipment_shop()
        elif answer == 3:
            pos = 2
            IF = 1
            menus.start_smithy()
        elif answer == 0:
            pos = 2
            IF = 1
        else:
            print("Неверное значение")

def start_food_shop(): #Стартовый продуктовый магазин
    print("Абоба")
def start_equipment_shop(): #Стартовый магазин экипировки
    print("Абобус")
def start_smithy(): #Стартовая кузница
    print("Агодус")
