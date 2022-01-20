import turtle
t = turtle.Turtle()
t.speed(0)

def hilbert(n): #angle is 60 degrees
    base = 'arbrc'
    a_seed = 'alblcrfa'
    b_seed = 'brclflarb'
    c_seed = 'cfralblc'
    if n==1:
        return base.replace('a', 'f').replace('b', 'f').replace('c', 'f')
    else:
        temp = seed.replace('f', hibert(n-1)).replace('rl', '').replace('lr', '')
        #temp2 = temp.replace('s', arrowhead_fractal(n-1).replace('r', 't').replace('l', 'r').replace('t', 'l')).replace('rl', '').replace('lr', '')
        return temp

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

turtledraw(carpet_fractal(5), 90, 2)
