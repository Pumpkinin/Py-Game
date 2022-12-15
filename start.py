import time
import event
import menus

health = 10 #Здоровье
gold = 10 #Золото

defense = 1 #Защита
speed = 1 #Скорость
lvl = 1 #Уровень
damage = 1 #Урон
exp = 0 #Опыт
max_exp = 100 #Максимальный опыт

print("Добро пожаловать в Fantasy Quest")
time.sleep(0)#2
print("Fantasy Quest - это фентезийная игра без графики и ещё чего либо.")
time.sleep(0)#4
print("Правила просты:")
print("Тут тебе надо будет зарабатывать деньги, развиваться, ходить в данжи и убивать монстров.")
print("Чтобы что-то выбрать, необходимо ввести число в скобках после желаемого варианта")
time.sleep(0)#7
print("Сразу говорю: иногда в программе чтобы что-то заработало нужно нажать 2 раза")
time.sleep(0)#3
print("Ну чтож, начнем!")
time.sleep(0)#3
print("Как тебя зовут, странник?")
name = input()
print("Приветствую тебя,", name)
time.sleep(0)#1
menus.start_menu()
