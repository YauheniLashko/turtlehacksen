import among_us
import pikachu
from turtle import *
from time import sleep


def tp(x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()


def hello():
    for i in lst:
        i.hideturtle()
    tp(0, 250, lst[0])
    lst[0].write("АЛГОРИТМИКА", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)

    tp(0, 200, lst[0])
    lst[0].write("IMPOSTOR GAMES 2024", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)

    tp(0, 150, lst[0])
    lst[0].write("Сделай клон любой известной игры", False, align="center", font=('Arial', 20, 'bold'))
    sleep(2)


def choice():
    lst[0].clear()
    lst[1].clear()
    tp(100, 0, lst[0])
    tp(-100, 0, lst[1])
    lst[0].write("Пикачу", False, align="center", font=('Arial', 20, 'bold'))
    lst[0].showturtle()
    lst[1].write("Among Us", False, align="center", font=('Arial', 15, 'bold'))
    lst[1].showturtle()
    tp(100, -20, lst[0])
    tp(-100, -20, lst[1])
    for i in range(2):
        for t in lst:
            t.forward(100)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(50)
  

lst = []
for i in range(2):
    t = Turtle()
    t.speed(0)
    t.shape('circle')
    lst.append(t)

hello()

choice()


def catch0(x, y):
    for i in lst:
        i.hideturtle()
        i.clear()
    pikachu.main()
    for i in lst:
        i.showturtle()
    choice()


def catch1(x, y):
    for i in lst:
        i.hideturtle()
        i.clear()
    among_us.draw()
    for i in lst:
        i.showturtle()
    choice()


lst[0].onclick(catch0)
lst[1].onclick(catch1)

exitonclick()
