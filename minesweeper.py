# Tony Southa south211
# I understand that this is a graded, individial examination that may not be
# discussed with anyone. I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing any aspect of the exam
# with anyone is academic misconduct and will result in failing the course.
# I further certify that this program represents my own work and that none of it
# was obtained from any source other than material presented as part of the
# course.

import turtle
import random

class Cell:

    def __init__(self,t,xmin,ymin,xmax,ymax):
        self.__t = t
        self.__xmin = xmin
        self.__ymin = ymin
        self.__xmax = xmax
        self.__ymax = ymax

        self.__bomb = False
        self.__cleared = False

    def isIn(self,x,y):
        if x in range(self.__xmin,self.__width+1) and y in range(self.__ymin,self.__height+1):
            return True
        return False

    def setBomb(self):
        self.__bomb = True

    def isBomb(self):
        if self.__bomb == True:
            return True
        return False

    def cleared(self):
        self.__cleared = True

    def isCleared(self):
        if self.__cleared == True:
            return True
        return False

    def showCount(self,c):
        self.__t.goto(self.__xmin + 7,self.__ymin)
        self.__t.write(c,font=("Arial",15,"bold"))

    def draw(self):
        self.__t.hideturtle()
        self.__t.speed(0)
        self.__t.penup()
        self.__t.goto(self.__xmin,self.__ymin)

        if self.__bomb == True:
            self.__t.fillcolor('red')
        elif self.__cleared == True:
            self.__t.fillcolor('dark gray')
        else:
            self.__t.fillcolor('green')

        self.__t.pendown()
        self.__t.begin_fill()
        self.__t.forward(self.__width-self.__xmin)
        self.__t.left(90)
        self.__t.forward(self.__height-self.__ymin)
        self.__t.left(90)
        self.__t.forward(self.__width-self.__xmin)
        self.__t.left(90)
        self.__t.forward(self.__height-self.__ymin)
        self.__t.left(90)
        self.__t.end_fill()

class Minesweeper:

    def __init__(self,rows,cols,mines,visible=False):
        self.__rows = rows
        self.__cols = cols
        self.__mines = mines
        self.__visible = visible
        self.__grid = []
        self.__t = turtle.Turtle()
        self.__s = self.__t.getscreen()

        ymin = -140
        ymax = -120
        for i in range(self.__rows):
            list_row = []
            xmin = -140
            xmax = -120
            for j in range(self.__cols):
                list_row.append(Cell(self.__t,xmin,ymin,xmax,ymax))
                xmin += 23
                xmax += 23
            self.__grid.append(list_row)
            ymin += 23
            ymax += 23

        turtle.tracer(0)
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__grid[i][j].draw()
        turtle.update()

        self.__s.onclick(self.getRowCol)
        self.__s.listen()

        i = 0
        while i < self.__mines:
            randx = random.randint(0,13)
            randy = random.randint(0,13)
            if self.__grid[randx][randy].isBomb() == False:
                self.__grid[randx][randy].setBomb()
                i += 1
                if self.__visible == True:
                    self.__grid[randx][randy].draw()

    def countBombs(self,row,col):
        neighborsx = [1,1,0,-1,-1,-1,0,1]
        neighborsy = [0,-1,-1,-1,0,1,1,1]
        bombs = 0

        for i in range(8):
            if neighborsx[i]+row in range(0,self.__rows):
                if neighborsy[i]+col in range(0,self.__cols):
                    if self.__grid[neighborsx[i]+row][neighborsy[i]+col].isBomb() == True:
                        bombs += 1
        return bombs

    def cellsRemaining(self):
        remaining = 0
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__grid[i][j].isCleared() == False:
                    if self.__grid[i][j].isBomb() == False:
                        remaining += 1
        return remaining

    def getRowCol(self,x,y):
        self.mouseClick(x,y)

    def mouseClick(self,x,y):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__grid[i][j].isIn(x,y) == True:
                    self.__grid[i][j].cleared()
                    if self.__grid[i][j].isBomb() == True:
                        self.gameOver()
                    else:
                        self.__grid[i][j].draw()
                        self.clearCell(i,j)

    def gameOver(self):
        for k in range(self.__rows):
            for l in range(self.__cols):
                if self.__grid[k][l].isBomb() == True:
                    self.__grid[k][l].draw()
                    self.__grid[k][l].showCount('*')
        self.__t.penup()
        self.__t.goto(-70,-200)
        self.__t.write('Game over',font=("Arial",35))
        self.__t.goto(-70,-230)
        self.__t.write('(click mouse to exit)',font=("Arial",20))
        self.__s.exitonclick()

    def clearCell(self,row,col):
        x = [1,1,0,-1,-1,-1,0,1]
        y = [0,-1,-1,-1,0,1,1,1]
        if self.cellsRemaining() == 0:
            self.win()
        elif self.countBombs(row,col) > 0:
                self.__grid[row][col].showCount(self.countBombs(row,col))
        else:
            for k in range(8):
                if x[k]+row in range(0,self.__rows):
                    if y[k]+col in range(0,self.__cols):
                        if self.__grid[x[k]+row][y[k]+col].isCleared() == False:
                            self.__grid[x[k]+row][y[k]+col].cleared()
                            self.__grid[x[k]+row][y[k]+col].draw()
                            self.clearCell(x[k]+row,y[k]+col)

    def win(self):
        for k in range(self.__rows):
            for l in range(self.__cols):
                if self.__grid[k][l].isBomb() == True:
                    self.__grid[k][l].draw()
                    self.__grid[k][l].showCount('*')
        self.__t.penup()
        self.__t.goto(-170,-200)
        self.__t.write('Congratulations! you win',font=("Arial",35))
        self.__t.goto(-70,-230)
        self.__t.write('(click mouse to exit)',font=("Arial",20))
        self.__s.exitonclick()

def main():
    Minesweeper(14,14,15)

if __name__ == '__main__':
    main()
