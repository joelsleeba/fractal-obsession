import turtle.Turtle() as t, random, math
t.clearscreen()
t.hideturtle()
t.speed(0)

vec_func = lambda x, y : (math.sin(y), math.sin(x))
#vec_func = lambda x, y : (math.sin(y), math.sin(x))

eucl_norm = lambda x, y: math.sqrt(x**2 + y**2)
taxi_norm = lambda x, y: abs(x)+abs(y)
max_norm = lambda x, y: max(abs(x), abs(y))

rad_to_deg = lambda x: 180*x/math.pi
cart_prod = lambda x,y: [(x[i], y[j]) for i in range(0, len(x)) for j in range(0, len(y))]

def cart_to_polar(x, y):
  r = eucl_norm(x, y)
  if x>0:
    degree = math.atan(y/x)
  elif x<0:
    degree = math.atan(y/x) + math.pi
  else:
    degree = math.pi/2 if y>0 else -1*math.pi/2
  return (r, degree)

def arrow(size, angle, wing, pencolor="green"):
  t.pencolor(pencolor)
  t.pendown()
  t.forward(size)
  t.left(angle)
  t.forward(wing)
  t.left(180)
  t.penup()
  t.forward(wing)
  t.right(2*angle-180)
  t.pendown()
  t.forward(wing)

def draw_arrow(point, length, direction):
  t.setheading(0)
  t.penup()
  t.goto(point[0], point[1])
  t.left(rad_to_deg(direction))
  pencolor = "blue"
  arrow(length, 135, 0.25*length, pencolor)

def vector_plot(vec_func, norm=eucl_norm, n_points=25, llx=-250, lly=-250, urx=250, ury=250):
  t.setworldcoordinates(llx, lly, urx, ury)

  xlist = [llx + i*(urx-llx)/n_points for i in range(n_points+1)]
  ylist = [lly + i*(ury-lly)/n_points for i in range(n_points+1)]
  gridpoints = cart_prod(xlist, ylist)
  for i in gridpoints:
    x, y = i
    xn, yn = vec_func(x, y)
    arrow_size, direction = cart_to_polar(xn, yn)
    draw_arrow((x, y), arrow_size/5, direction)
  t.hideturtle()
  t.done()

size = 10
vector_plot(vec_func, eucl_norm, n_points=80, llx=-1*size, lly=-1*size, urx=size, ury=size)
