import turtle, random
t = turtle.Turtle()
t.speed(0)

A = (-250, -250)
B = (250, -250)
C = (0, 183.012701892)

t.penup()
X = (250, -250)
mid = lambda i, j: (i+j)/2

for i in range(100000):
    r = random.randint(1, 3)
    if r==1:
      X = tuple(map(mid, A, X))
    elif r==2:
      X = tuple(map(mid, B, X))
    else:
      X = tuple(map(mid, C, X))

    t.goto(X)
    t.dot(1, 'green')
