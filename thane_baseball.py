# Conor Thane
# Cs 21, Fall Semester
# Final Project: Baseball Simulator

""" This module is designed to be a mini baseball simulator.The idea is that
a baseball field will be drawn with concrete dimensions.There are predetermined
spots that are considered hits and outs. Different spots correspond with single,
double, triple, homerun, or out. Based on the radius of the line and the angle
the ball will be recorded as result. The inning ends after 3 outs. The result
goes into the scoreboard and then scores the games outs and runs. The outs and
runs are then shown and printed by the ballgame function."""
from graphics import *
import math
import random

""" The create_field function is designed to make a graphic that represents a
baseball field with predetermined dimensions, bases, foul lines, and a mound."""


def print_intro():
# This function just prints the intro to the game.
    print("This is a baseball inning simulator. It will simulate an inning of \
baseball and return the number of outs and the number of runs \
scored.")


    
def create_field_play_ball():
# In order to play the dimensions of the game need to be set and the graphics
# window created so the first half of this is creating the field.
    gw = GraphWin("Field", 300,400)
    gw.setBackground("green")

    homeplate = Point(150,399)
    leftpole = Point(0,125)
    rightpole = Point(299,125)
    leftline = Line(homeplate,leftpole)
    rightline= Line(homeplate,rightpole)
    leftline.setFill("white")
    rightline.setFill("white")
    rightpole.setFill("yellow")
    leftpole.setFill("yellow")
    leftline.draw(gw)
    rightline.draw(gw)
    rightpole.draw(gw)
    leftpole.draw(gw)
    moundpoint = Point(150, 325)
    mound = Circle(moundpoint,10)
    mound.setFill("brown")
    mound.draw(gw)
    rubber = Rectangle(Point(147,324),Point(153,326))
    rubber.setFill("white")
    rubber.draw(gw)
    base2 = Rectangle(Point(147,273),Point(153,277))
    base2.setFill("white")
    base2.draw(gw)
    base3 = Rectangle(Point(108,323),Point(114,327))
    base3.setFill("white")
    base3.draw(gw)
    base1 = Rectangle(Point(186,323),Point(192,327))
    base1.setFill("white")
    base1.draw(gw)
# An open list is made to record the random result after each hit.
# The loop runs until there are three outs.
    runners = []
    outs = 0
    while outs < 3:
        key = gw.checkKey()
        if key == "q":
            break
        else:
            p = Point(random.randrange(0,300), random.randrange(0,400))
        if math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY()) - \
        homeplate.getY())**2) <= 20:
            outs += 1
        elif 20 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY()) - \
        homeplate.getY())**2) <= 40:
            runners.append(1)
        elif 40 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY()) - \
        homeplate.getY())**2)  <= 150:
            outs += 1
        elif 150 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY())- \
        homeplate.getY())**2) <= 190:
            runners.append(1)
        elif 190 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY())- \
        homeplate.getY())**2) <= 280:
            outs += 0
        elif 280 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY())- \
        homeplate.getY())**2) <= 305:
            runners.append(2)
        elif 305 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY())- \
        homeplate.getY())**2) <= 325:
            runners.append(3)
        elif 325 < math.sqrt(((p.getX()) - homeplate.getX())**2 + ((p.getY())- \
        homeplate.getY())**2) <= 399:
            runners.append(4)
        ball = Circle(p,5)
        ball.setFill("white")
        ball.draw(gw)
        print("runners", runners)
        print("outs", outs)
    return runners


def scoreboard(runners):
# The scoreboard takes the list and looks at the last three numbers depending
# on if one reaches 4 then all the numbers before turn into runs since those
# runners must score.
    runs = 0
    outs = 3
    end = 0
    if len(runners) < 3:
        runs = 0
    elif runners[-1] == 4:
        runs = len(runners)
    elif runners[-1] + runners[-2] >= 4:
        runs = len(runners) - 1
    elif runners[-1] + runners[-2] + runners[-3] >= 4:
        runs = len(runners) - 2
    else:
        runs = 0
    
    return runs
    


def ballgame(runs):
# This function just prints the result. 
    print("During the inning the team scored", runs, "runs")
    
        
def main():

    print_intro()
    runners = create_field_play_ball()
    runs = scoreboard(runners)
    ballgame(runs)

main()

    
                    
        



