import matplotlib.pyplot as plt
import math, random

L = 7
t = ''
s = ''
p = ''
h = ''
num = 0
ptlist = []

#a = (0, math.sqrt(3)*L/4)
#b = (-L/2, -math.sqrt(3)*L/4)
#c = (L/2, -math.sqrt(3)*L/4)

x = (0,0)

xvals = []
yvals = []

N = int(input("Enter the number of iterations: "))
shape = str(input("Enter what n-gon you desire (3 for triangle, 4 for square, and so on): "))
while True:
    if shape == '3' or shape == '4' or shape == '5' or shape == '6' or shape == '7':
        break
    shape = input("Sorry, wrong input. Try again: ")
i = 0

if shape == '3':
    num = 3
    a = (0, math.sqrt(3) * L / 4)
    b = (-L / 2, -math.sqrt(3) * L / 4)
    c = (L / 2, -math.sqrt(3) * L / 4)
if shape == '4':
    num = 4
    a = (-L, L)
    b = (L, L)
    c = (L, -L)
    d = (-L, -L)
if shape == '5': #http://mathworld.wolfram.com/RegularPentagon.html
    num = 5
    a = (0, 1)
    b = (math.sin(2* math.pi/5), math.cos(2 * math.pi/5))
    c = (math.sin(4* math.pi/5), -math.cos(math.pi/5))
    d = (-math.sin(4* math.pi/5), -math.cos(math.pi/5))
    e = (-math.sin(2*math.pi/5), math.cos(2*math.pi/5))
if shape == '6': #http://mathworld.wolfram.com/RegularHexagon
    num = 6
    a = (0, 1)
    b = (math.cos(math.pi/6), math.sin(math.pi/6))
    c = (math.cos(math.pi/6), -math.sin(math.pi/6))
    d = (0,-1)
    e = (-math.cos(math.pi/6), -math.sin(math.pi/6))
    f = (-math.cos(math.pi/6), math.sin(math.pi/6))
if shape == '7': #http://mathworld.wolfram.com/RegularHeptagon
    num = 7
    a = (0, 1)
    b = (math.cos(3*math.pi/14), math.sin(3*math.pi/14))
    c = (math.cos(math.pi/14), -math.sin(math.pi/14))
    d = (math.sin(math.pi/7), -math.cos(math.pi/7))
    e = (-math.sin(math.pi/7), -math.cos(math.pi/7))
    f = (-math.cos(math.pi/14), -math.sin(math.pi/14))
    g = (-math.cos(3*math.pi/14), math.sin(3*math.pi/14))

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
    if r == 5:
        x = midpoint(a[0], a[1], f[0], f[1])
    if r == 6:
        x = midpoint(a[0], a[1], g[0], g[1])
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
    if r == 5:
        x = midpoint(b[0], b[1], f[0], f[1])
    if r == 6:
        x = midpoint(b[0], b[1], g[0], g[1])
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
    if r == 5:
        x = midpoint(c[0], c[1], f[0], f[1])
    if r == 6:
        x = midpoint(c[0], c[1], g[0], g[1])
if r == 4:
    #D is chosen as the fourth pt
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(d[0], d[1], a[0], a[1])
    if r == 2:
        x = midpoint(d[0], d[1], b[0], b[1])
    if r == 3:
        x = midpoint(d[0], d[1], c[0], c[1])
    if r == 4:
        x = midpoint(d[0], d[1], e[0], e[1])
    if r == 5:
        x = midpoint(d[0], d[1], f[0], f[1])
    if r == 6:
        x = midpoint(d[0], d[1], g[0], g[1])
if r == 5:
    #E is chosen as the fifth pt
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(e[0], e[1], a[0], a[1])
    if r == 2:
        x = midpoint(e[0], e[1], b[0], b[1])
    if r == 3:
        x = midpoint(e[0], e[1], c[0], c[1])
    if r == 4:
        x = midpoint(e[0], e[1], d[0], d[1])
    if r == 5:
        x = midpoint(e[0], e[1], f[0], f[1])
    if r == 6:
        x = midpoint(e[0], e[1], g[0], g[1])
if r == 6:
    #F is chosen as the sixth pt
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(f[0], f[1], a[0], a[1])
    if r == 2:
        x = midpoint(f[0], f[1], b[0], b[1])
    if r == 3:
        x = midpoint(f[0], f[1], c[0], c[1])
    if r == 4:
        x = midpoint(f[0], f[1], d[0], d[1])
    if r == 5:
        x = midpoint(f[0], f[1], e[0], e[1])
    if r == 6:
        x = midpoint(f[0], f[1], g[0], g[1])
if r == 7:
    #G is chosen as the seventh pt
    r = random.randint(1,num - 1)
    if r == 1:
        x = midpoint(g[0], g[1], a[0], a[1])
    if r == 2:
        x = midpoint(g[0], g[1], b[0], b[1])
    if r == 3:
        x = midpoint(g[0], g[1], c[0], c[1])
    if r == 4:
        x = midpoint(g[0], g[1], d[0], d[1])
    if r == 5:
        x = midpoint(g[0], g[1], e[0], e[1])
    if r == 6:
        x = midpoint(g[0], g[1], f[0], f[1])

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
    if r == 5: #E
        x = midpoint(x[0], x[1], e[0], e[1])
    if r == 6: #F
        x = midpoint(x[0], x[1], f[0], f[1])
    if r == 7: #G
        x = midpoint(x[0], x[1], g[0], g[1])
    xvals.append(x[0])
    yvals.append(x[1])
    i += 1

plt.scatter(xvals, yvals,s = 0.5, c = "r", marker = "o")
plt.title("Chaos Game")
plt.axis('off')
plt.tight_layout()

plt.show(block = True)

