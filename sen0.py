import among_us
import pikachu
from turtle import *
from time import sleep


def tp(x, y):
    penup()
    goto(x, y)
    pendown()


def hello():
    color('purple')
    hideturtle()
    tp(0, 250)
    write("АЛГОРИТМИКА", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)

    tp(0, 200)
    write("IMPOSTOR GAMES 2024", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)

    tp(0, 150)
    write("Сделай клон любой известной игры", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)

speed(0)

hello()
clear()
choice = input("1 - нарисовать пикачу, 2 - нарисовать героя among us, 3 - выйти")
while choice != '3':
    if choice == '1':
        pikachu.main()
    elif choice == '2':
        among_us.draw()
    elif choice == '3':
        break
    else:
        print('Повторите ввод')
    choice = input("1 - нарисовать пикачу, 2 - нарисовать героя among us, 3 - выйти")



exitonclick()
