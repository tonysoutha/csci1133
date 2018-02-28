import turtle
import random
import time

def pins(pin):
    if pin == 0:
        turtle.goto(0,-80)
    if pin == 1:
        turtle.goto(-30,-40)
    if pin == 2:
        turtle.goto(30,-40)
    if pin == 3:
        turtle.goto(-60,0)
    if pin == 4:
        turtle.goto(0,0)
    if pin == 5:
        turtle.goto(60,0)
    if pin == 6:
        turtle.goto(-90,40)
    if pin == 7:
        turtle.goto(-30,40)
    if pin == 8:
        turtle.goto(30,40)
    if pin == 9:
        turtle.goto(90,40)

def knocked_over(pin):
    if pin == 0:
        turtle.goto(-5,-92)
    if pin == 1:
        turtle.goto(-35,-52)
    if pin == 2:
        turtle.goto(25,-52)
    if pin == 3:
        turtle.goto(-65,-12)
    if pin == 4:
        turtle.goto(-5,-12)
    if pin == 5:
        turtle.goto(55,-12)
    if pin == 6:
        turtle.goto(-95,28)
    if pin == 7:
        turtle.goto(-35,28)
    if pin == 8:
        turtle.goto(25,28)
    if pin == 9:
        turtle.goto(85,28)

def makeboard(standing):
    turtle.clear()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color('Blue')
    turtle.shape('circle')
    turtle.penup()
    i = 0
    for i in range(10):
        pins(i)
        turtle.stamp()
        standing.append(i)

def play1(move1,standing):
    random.shuffle(standing)
    i = 0
    if move1 == 10:
        for each in range(10):
            pins(standing[each])
            turtle.color('white')
            turtle.stamp()
            knocked_over(standing[each])
            turtle.color('black')
            turtle.write('X',font = ('arial',20))
        turtle.goto(0,-140)
        turtle.color('red')
        turtle.write('Strike!',align='center',font = ('arial',30,))
        #time.sleep(2)
    else:
        while i < move1:
            pins(standing[i])
            turtle.color('white')
            turtle.stamp()
            knocked_over(standing[i])
            turtle.color('black')
            turtle.write('X',font = ('arial',20))
            i += 1

def play2(move1,move2,standing):
    if move2 == 10 - move1:
        i = int(move1)
        while i < 10:
            pins(standing[i])
            turtle.color('white')
            turtle.stamp()
            knocked_over(standing[i])
            turtle.color('black')
            turtle.write('X',font = ('arial',20))
            i += 1
        turtle.goto(0,-140)
        turtle.color('red')
        turtle.write('Spare',align='center',font = ('arial',30,))
        #time.sleep(2)
    else:
        i = int(move1)
        while i < move1 + move2:
            pins(standing[i])
            turtle.color('white')
            turtle.stamp()
            knocked_over(standing[i])
            turtle.color('black')
            turtle.write('X',font = ('arial',20))
            i += 1
        turtle.goto(0,-140)
        turtle.color('red')
        turtle.write('Open Frame: ' + str(10-(move1+move2)),align='center',font = ('arial',30,))
        #time.sleep(2)

def finalScore(pinlist):
    scorelist = []
    rolls = 0
    scores = 0
    while rolls < len(pinlist):
        if rolls == len(pinlist)-1:
            scorelist.append(pinlist[rolls])
            rolls += 1
            scores += 1
        elif pinlist[rolls] == 10:
            scorelist.append(10)
            scorelist[scores] += pinlist[rolls+1]
            if rolls != len(pinlist)-2:
                scorelist[scores] += pinlist[rolls+2]
            rolls += 1
            scores += 1
        elif pinlist[rolls] + pinlist[rolls+1] == 10:
            scorelist.append(10)
            scorelist[scores] += pinlist[rolls+2]
            rolls += 2
            scores += 1
        else:
            scorelist.append(pinlist[rolls])
            scorelist[scores] += pinlist[rolls+1]
            rolls += 2
            scores += 1
    return sum(scorelist)

def writescore(finalscore):
    turtle.undo()
    turtle.goto(0,-140)
    turtle.color('red')
    turtle.write('Final Score: ' + finalscore,align='center',font = ('arial',30,))

def main():
    pinlist = []
    frame = 1
    while frame <= 11:
        standing = []
        makeboard(standing)
        if frame != 10 or pinlist[-1] == 10 or pinlist[-1] + pinlist[-2] == 10:
            move1 = turtle.textinput('Frame ' + str(frame),'Enter # of pins (null for random)')
            if move1 == '':
                move1 = random.randint(0,10)
            if int(move1) > 10:
                move1 = 10
            move1 = int(move1)
            play1(move1,standing)
            pinlist.append(move1)
            if move1 != 10:
                move2 = turtle.textinput('Frame ' + str(frame),'Enter # of pins (null for random)')
                if move2 == '':
                    move2 = random.randint(0,move1)
                if int(move2) > 10 - move1:
                    move2 = 10 - move1
                move2 = int(move2)
                play2(move1,move2,standing)
                pinlist.append(move2)
        frame += 1
    finalscore = str(finalScore(pinlist))
    writescore(finalscore)

if __name__ == '__main__':
    main()
