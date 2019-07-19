import matplotlib.pyplot as plt
import math,random

def main():
    i, ptlist, xvals, yvals = 0, [], [], []
    numiter = int(input("Enter the number of iterations: "))
    numsides = int(input("Enter the number of sides (Not Too Many - Creates a Circle): "))
    
    while True:
        if numsides > 3 and type(numsides) == int:
            break
        numsides = input("Sorry, wrong input. Try again: ")

    rotation = int(input("Enter the degrees of rotation: "))
    while True:
        if 0 <= rotation <= 360:
            break
        rotation = int(input("Sorry, invalid output. Try again: "))
    rotation *= math.pi / 180  # https://en.wikipedia.org/wiki/Rotation_of_axes

    def pointfinder(N,n):
        x = math.cos(2*math.pi*n/N)
        y = math.sin(2*math.pi*n/N)
        return (x*math.cos(rotation) + y*math.sin(rotation), -x*math.sin(rotation) + y*math.cos(rotation))
    
    def midpoint(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

    for i in range(0, numsides):
        ptlist.append(pointfinder(numsides, i))

    def midpoint(x1, y1, x2, y2):
        return ((x2 + x1) / 2, (y2 + y1 / 2))

    r = random.randint(1, numsides)
    x = midpoint(ptlist[r - 1][0], ptlist[r - 1][0], ptlist[random.randint(0, numsides - 1)][0],
                 ptlist[random.randint(0, numsides - 1)][1])

    while i < numiter:
        r = random.randint(1, numsides)
        x = midpoint(x[0], x[1], ptlist[r - 1][0], ptlist[r - 1][1])
        xvals.append(x[0])
        yvals.append(x[1])
        i += 1

    plt.scatter(xvals, yvals, s = 0.5, c = "r", marker = "o")
    plt.title("Chaos Game")
    plt.axis('off')
    #plt.tight_layout()
    plt.show(block = True)

if __name__ == "__main__":
    main()