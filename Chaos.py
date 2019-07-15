import matplotlib.pyplot as plt
import math, random

L = 5
t = ''
s = ''
p = ''
num = 0

#a = (0, math.sqrt(3)*L/4)
#b = (-L/2, -math.sqrt(3)*L/4)
#c = (L/2, -math.sqrt(3)*L/4)

x = (0,0)

xvals = []
yvals = []

N = int(input("Enter the number of iterations: "))
shape = str(input("Enter what shape you desire (t for triangle, s for square, p for pentagon): "))
while True:
    if shape == 't' or shape == 's' or shape == 'p':
        break
    shape = input("Sorry, wrong input. Try again: ")
i = 0

if shape == 't':
    num = 3
    a = (0, math.sqrt(3) * L / 4)
    b = (-L / 2, -math.sqrt(3) * L / 4)
    c = (L / 2, -math.sqrt(3) * L / 4)
if shape == 's':
    num = 4
    a = (-L, L)
    b = (L, L)
    c = (L, -L)
    d = (-L, -L)
if shape == 'p': #http://mathworld.wolfram.com/RegularPentagon.html
    num = 5
    a = (0, 1)
    b = (math.sin(2* math.pi/5), math.cos(2 * math.pi/5))
    c = (math.sin(4* math.pi/5), -math.cos(math.pi/5))
    d = (-math.sin(4* math.pi/5), -math.cos(math.pi/5))
    e = (-math.sin(2*math.pi/5), math.cos(2*math.pi/5))

def midpoint(x1, y1, x2, y2):
    return ((x2 + x1) / 2, (y2 + y1 / 2))

r = random.randint(1,num)

if r == 1:
    # A is chosen as first point
    r = random.randint(1,num - 1)
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
    r = random.randint(1,num - 1)
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
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(c[0], c[1], a[0], a[1])
    if r == 2:
        x = midpoint(c[0], c[1], b[0], b[1])
    if r == 3:
        x = midpoint(c[0], c[1], d[0], d[1])
    if r == 4:
        x = midpoint(c[0], c[1], e[0], e[1])
if r == 4:
    #C is chosen as the fourth pt
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(d[0], d[1], a[0], a[1])
    if r == 2:
        x = midpoint(d[0], d[1], b[0], b[1])
    if r == 3:
        x = midpoint(d[0], d[1], c[0], c[1])
    if r == 4:
        x = midpoint(d[0], d[1], d[0], d[1])
if r == 5:
    #C is chosen as the fifth pt
    r = random.randint(1,num - 1)
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

while i < N:
    r = random.randint(1,num)
    if r == 1: #A
        x = midpoint(x[0],x[1],a[0],a[1])
    if r == 2: #B
        x = midpoint(x[0], x[1], b[0], b[1])
    if r == 3: #C
        x = midpoint(x[0], x[1], c[0], c[1])
    if r == 4: #D
        x = midpoint(x[0], x[1], d[0], d[1])
    if r == 5: #C
        x = midpoint(x[0], x[1], e[0], e[1])
    xvals.append(x[0])
    yvals.append(x[1])
    i += 1

plt.scatter(xvals, yvals,s = 0.5, c = "r", marker = "o")
plt.title("Chaos Game")
plt.axis('off')
plt.tight_layout()

plt.show(block = True)