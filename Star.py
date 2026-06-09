import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for _ in range(5):
        t.forward(50)
        t.right(144)

s = turtle.Screen()
s.onscreenclick(draw_star)

turtle.done()
