import turtle, random, math
t = turtle.Turtle()
t.speed(0)

def cartesian_to_polar(r, theta):
  return (r*math.cos(theta), r*math.sin(theta))

def reg_polygon_points(n, r):
  return [cartesian_to_polar(r, 2*i*math.pi/n) for i in range(n)]

def chaos_game(n, r):
  t.penup()
  points = reg_polygon_points(n, r)
  X = points[0]
  mid = lambda i, j: (i+j)/(n-1)

  for i in range(100000):
    r = random.randint(1, n)
    X = tuple(map(mid, points[r-1], X))

    t.goto(X)
    t.dot(2, 'green')
    
chaos_game(3, 100)
