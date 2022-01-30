import turtle.Turtle() as t, random, math
t.clearscreen()
t.speed(0)

t.hideturtle()
func = lambda x, y: abs(complex(x, y))/100
#func = lambda x, y: x

def polar_to_cartesian(r, theta):
  return (r*math.cos(theta), r*math.sin(theta))

def cartesian_to_polar(x, y):
  return (x**2+y**2, math.atan(y/x))

def fcolor(x, xmax):
  y = 256*(x/math.log(x))/(xmax/math.log(xmax))
  color = (int(y)%256, 0, int(256-y)%256)
  return color

def arrow(size, angle, wing):
  t.forward(size)
  t.left(angle)
  t.forward(wing)
  t.left(180)
  t.penup()
  t.forward(wing)
  t.right(2*angle-180)
  t.pendown()
  t.forward(wing)

def randomwalk(func, step, size, n):
  t.penup()
  for i in range(n):
    t.setheading(0)
    x, y = random.randint(-1*size, size), random.randint(-1*size, size)
    t.goto(x, y)
    
    fmax = func(size, size)
    direction = func(x, y)
    xdel, ydel = polar_to_cartesian(step, direction)
    stepsize = step*(func(x+xdel, y+ydel) - func(x-xdel, y-ydel))/(2*func(xdel, ydel))
    #color = fcolor(fmax, direction)

    t.pencolor("blue" if stepsize>0 else "red")
    t.pendown()
    t.left(direction)
    arrow(stepsize, 135, 0.25*stepsize)
    t.penup()
  t.done()

randomwalk(func, 12, 250, 3000)
