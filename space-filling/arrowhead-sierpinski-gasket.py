import turtle
t = turtle.Turtle()
t.speed(0)

def arrowhead_fractal(n): #angle is 60 degrees
    seed = 'lsrfrsl'
    if n==1:
        return seed.replace('s', 'f')
    else:
        temp = seed.replace('f', arrowhead_fractal(n-1)).replace('rl', '').replace('lr', '')
        temp2 = temp.replace('s', arrowhead_fractal(n-1).replace('r', 't').replace('l', 'r').replace('t', 'l')).replace('rl', '').replace('lr', '')
        return temp2

def turtledraw(x, angle, step):
    t.penup()
    t.setpos(-250, -250)
    t.pendown()
    for i in x:
        if i=='f':
            t.forward(step)
        elif i=='r':
            t.right(angle)
        elif i=='l':
            t.left(angle)

turtledraw(arrowhead_fractal(8), 60, 2)
