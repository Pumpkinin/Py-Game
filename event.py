import menus

def promocode(): #Промокоды
    print("Есть промокод?")
    answer = input()
    option = ["Есть", "есть", "Да", "да"]
    gold10000 = 0 #1 промокод
    while answer in option:
        print("Вводи промокод")
        promo = input()
        if promo == 'gold10000':
            if gold10000 == 0: #Начало 1 промокода
                gold = gold + 10000
                print("+ 10000 Золота")
                gold10000 = 1
            else:
                print("Промокод уже использован, попробуй другой") #Конец 1 промокода
        else:
            print("Неверный промокод")
        print("Если закончились промокоды напиши нету, а если остались, то напиши есть")
        answer = input()

def change_name(): #Смена имени
    print("Введи новое имя:")
    name = input()

def back_to(): #Возращение к предыдущему меню
    if pos == 0:
        menus.start_menu()
    elif pos == 1:
        menus.profile()
    elif pos == 2:
        menus.start_city()
