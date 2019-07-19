import matplotlib.pyplot as plt
import math, random

num, ptlist, x, xvals, yvals = 0, [], (0,0), [], []

N = int(input("Enter the number of iterations: "))
shape = input("Enter the number of sides of the n-gon: ")
while True:
    if shape.isnumeric():
        shape = int(shape)
        break
    shape = input("Sorry, wrong input. Try again: ")
i = 0

num = shape
for i in range(0, shape):
    ptlist.append((math.cos(i*2*math.pi/shape), math.sin(i*2*math.pi/shape)))

def midpoint(x1, y1, x2, y2):
    return ((x2 + x1) / 2, (y2 + y1 / 2))

r = random.randint(1,num)
x = midpoint(ptlist[r-1][0], ptlist[r-1][0], ptlist[random.randint(0, num-1)][0], ptlist[random.randint(0, num-1)][1])

while i < N:
    r = random.randint(1,num)
    x = midpoint(x[0], x[1], ptlist[r-1][0], ptlist[r-1][1])
    xvals.append(x[0])
    yvals.append(x[1])
    i += 1

plt.scatter(xvals, yvals,s = 0.5, c = "r", marker = "o")
plt.title("Chaos Game")
plt.axis('off')
plt.tight_layout()
plt.show(block = True)
