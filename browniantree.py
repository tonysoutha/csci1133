# Tony Southa south211
# I understand that this is a graded, individual examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

import turtle
import random
import math

def hasNeighbor(grid,row,col):
    valid = False
    if row > 199 or col > 199:
        return valid
    else:
        e = grid[row+1][col]
        n = grid[row][col+1]
        ne = grid[row+1][col+1]
        w = grid[row-1][col]
        s = grid[row][col-1]
        sw = grid[row-1][col-1]
        se = grid[row+1][col-1]
        nw = grid[row-1][col+1]

        if row == 0 and col == 0:
            loc = [e,n,ne]
        elif row == 0 and col == 199:
            loc = [e,s,se]
        elif row == 199 and col == 0:
            loc = [w,n,nw]
        elif row == 199 and col == 199:
            loc = [w,s,sw]

        elif row in range(1,199) and col == 0:
            loc = [n,e,w,ne,nw]
        elif row in range(1,199) and col == 199:
            loc = [s,e,w,se,sw]
        elif row == 0 and col in range(1,199):
            loc = [n,s,e,ne,se]
        elif row == 199 and col in range(1,199):
            loc = [n,s,w,nw,sw]
        else:
            loc = [n,s,e,w,ne,nw,se,sw]

        for each in loc:
            if each == True:
                if grid[row][col] == False:
                    valid = True
        return valid

def origin(grid,particles):
    turtle.setworldcoordinates(0,0,199,199)
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)
    if particles != -1:
        turtle.goto(100,100)
        turtle.color('blue')
        turtle.dot(5)
        grid[100][100] = True

def createparticle(R,grid,particles):
    turtle.hideturtle()
    turtle.speed(0)
    a = random.randint(0,360)
    x = int(((math.cos(a * (math.pi / 180))*R) + 100 + 0.5))
    y = int(((math.sin(a * (math.pi / 180))*R) + 100 + 0.5))

    if particles == 0 or particles == -1:
        turtle.forward(0)
    else:
        randang = [0,90,180,270]
        x2 = int(math.cos(random.choice(randang) * (math.pi / 180)) + 0.5 + x)
        y2 = int(math.sin(random.choice(randang) * (math.pi / 180)) + 0.5 + y)

        steps = 0
        while hasNeighbor(grid,x2,y2) == False and steps < 200:
            x2 = int(math.cos(random.choice(randang) * (math.pi / 180)) + 0.5 + x2)
            y2 = int(math.sin(random.choice(randang) * (math.pi / 180)) + 0.5 + y2)
            steps += 1

        if steps == 200:
            createparticle(R,grid,particles)
        else:
            turtle.goto(x2,y2)
            turtle.dot(5)
            grid[x2][y2] = True
            if int((((abs(x2)-100) ** 2 + (abs(y2)-100) **2) ** 0.5) + 0.5) > R:
                createparticle(R+1,grid,particles-1)
            else:
                createparticle(R,grid,particles-1)

def main():
    R = 1
    grid = []
    for i in range(200):
        grid.append([False]*200)
    particles = int(turtle.textinput('','Enter tree size: ')) - 1
    origin(grid,particles)
    createparticle(R,grid,particles)

if __name__ == '__main__':
    main()
