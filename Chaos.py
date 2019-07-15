import matplotlib.pyplot as plt
import math, random

t = ''
s = ''
p = ''
i = 0
a, b, c, d, e = (0,0), (0,0), (0,0), (0,0), (0,0)

xvals = []
yvals = []

numiter = int(input("Enter the number of iterations: "))
shape = str(input("Enter what shape you desire (t for triangle, s for square, p for pentagon): "))
while True:
    if shape == 't' or shape == 's' or shape == 'p':
        break
    shape = input("Sorry, wrong input. Try again: ")
rotation = int(input("Enter the degrees of rotation: "))
while True:
    if 0 <= rotation <= 360:
        break
    shape = int(input("Sorry, invalid output. Try again: "))

rotation *= math.pi/180 #https://en.wikipedia.org/wiki/Rotation_of_axes

def pointfinder(N,n):
    x = math.cos(2*math.pi*n/N)
    y = math.sin(2*math.pi*n/N)
    return (x*math.cos(rotation) + y*math.sin(rotation), -x*math.sin(rotation) + y*math.cos(rotation))

def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

if shape == 't':
    N = 3
    a, b, c = pointfinder(N,0), pointfinder(N,1), pointfinder(N,2)

if shape == 's':
    N = 4
    a, b, c, d = pointfinder(N,0), pointfinder(N,1), pointfinder(N,2), pointfinder(N,3)

if shape == 'p':
    # http://mathworld.wolfram.com/RegularPentagon.html
    N = 5
    a, b, c, d, e = pointfinder(N, 0), pointfinder(N, 1), pointfinder(N, 2), pointfinder(N, 3), pointfinder(N, 4)

r = random.randint(1,N)

if r == 1:
    # A is chosen as first point
    r = random.randint(1,N - 1)
    if r == 1:
        x = midpoint(a[0], a[1], b[0], b[1])
    if r == 2:
        x = midpoint(a[0], a[1], c[0], c[1])
    if r == 3:
        x = midpoint(a[0], a[1], d[0], d[1])
    if r == 4:
        x = midpoint(a[0], a[1], e[0], e[1])
if r == 2:
    # B is chosen as the second pt
    r = random.randint(1,N - 1)
    if r == 1:
        x = midpoint(b[0], b[1], a[0], a[1])
    if r == 2:
        x = midpoint(b[0], b[1], c[0], c[1])
    if r == 3:
        x = midpoint(b[0], b[1], d[0], d[1])
    if r == 4:
        x = midpoint(b[0], b[1], e[0], e[1])
if r == 3:
    #C is chosen as the third pt
    r = random.randint(1,N - 1)
    if r == 1:
        x = midpoint(c[0], c[1], a[0], a[1])
    if r == 2:
        x = midpoint(c[0], c[1], b[0], b[1])
    if r == 3:
        x = midpoint(c[0], c[1], d[0], d[1])
    if r == 4:
        x = midpoint(c[0], c[1], e[0], e[1])
if r == 4:
    #D is chosen as the fourth pt
    r = random.randint(1,N - 1)
    if r == 1:
        x = midpoint(d[0], d[1], a[0], a[1])
    if r == 2:
        x = midpoint(d[0], d[1], b[0], b[1])
    if r == 3:
        x = midpoint(d[0], d[1], c[0], c[1])
    if r == 4:
        x = midpoint(d[0], d[1], e[0], e[1])
if r == 5:
    #E is chosen as the fifth pt
    r = random.randint(1,N - 1)
    if r == 1:
        x = midpoint(e[0], e[1], a[0], a[1])
    if r == 2:
        x = midpoint(e[0], e[1], b[0], b[1])
    if r == 3:
        x = midpoint(e[0], e[1], c[0], c[1])
    if r == 4:
        x = midpoint(e[0], e[1], d[0], d[1])

#xvals.append(x[0])
#yvals.append(x[1])

while i < numiter:
    r = random.randint(1,N)
    if r == 1: #A
        x = midpoint(x[0], x[1], a[0], a[1])
    if r == 2: #B
        x = midpoint(x[0], x[1], b[0], b[1])
    if r == 3: #C
        x = midpoint(x[0], x[1], c[0], c[1])
    if r == 4: #D
        x = midpoint(x[0], x[1], d[0], d[1])
    if r == 5: #E
        x = midpoint(x[0], x[1], e[0], e[1])
    xvals.append(x[0])
    yvals.append(x[1])
    i += 1

plt.scatter(xvals, yvals, s = 0.5, c = "r", marker = "o")
plt.title("Chaos Game")
plt.axis('off')
#plt.tight_layout()
plt.show(block = True)