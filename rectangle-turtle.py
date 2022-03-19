import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Triangle():
    for i in range(10):
        tao.forward(100)
        tao.left(120)
        tao.forward(100)
        tao.left(120)
        tao.forward(100)
        tao.left(45)

def Cycle():
    c = ['black','gray','green','blue','violet','yellow','orange','brown','magenta','cyan']
    for i in range(10):
        tao.color(c[i])
        n =10
        while n <= 50:
            tao.circle(n)
            n = n+10
        tao.left(36)

def OuterCycle(n):
    tao.pen(pencolor="red", pensize=2)
    tao.color("red")
    tao.circle(n)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Cycle()
Go(0,-100)
OuterCycle(100)

