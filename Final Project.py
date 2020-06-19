#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Final Project


from turtle import *
import random
import time 
ryan = Turtle()
ryan.speed(1000)
screen = ryan.getscreen()


class Tank:
    def __init__(self, reloadRate, accuracy, armor, power):
        self.reloadRate = reloadRate
        self.accuracy = accuracy
        self.armor = armor
        self.power = power
        self.health = 10
        self.morale = 1.0

def drawBox(x,y,width,height,color):
    ryan.penup()
    ryan.goto(x,y)
    ryan.pendown()
    ryan.color("black",color)
    ryan.begin_fill()
    ryan.goto(x+width,y)
    ryan.goto(x+width,y+height)
    ryan.goto(x,y+height)
    ryan.goto(x,y)
    ryan.end_fill()
    ryan.penup()

def drawTank(side, color):
    if side == "left":
        drawBox(-200, 0, 100, 50, color)
        drawBox(-180, 50, 60, 30, color)
        drawBox(-120, 60, 30, 10, color)
    if side == "right":
        drawBox(50, 0, 100, 50, color)
        drawBox(70, 50, 60, 30, color)
        drawBox(40, 60, 30, 10, color)

logPos = 100
def log(string):
    global logPos
    ryan.penup()
    ryan.goto(300, logPos)
    ryan.write(string)
    logPos = logPos - 10

    
reloadRate = int (input("Enter Tank 1 (Reload Rate):"))
accuracy = int (input("Enter Tank 1 (Accuracy):"))
armor = int (input("Enter Tank 1 (Armor):"))
power = int (input("Enter Tank 1 (Power):"))
tank1 = Tank(reloadRate, accuracy, armor, power)

reloadRate = int (input("Enter Tank 2 (Reload Rate):"))
accuracy = int (input("Enter Tank 2 (Accuracy):"))
armor = int (input("Enter Tank 2 (Armor):"))
power = int (input("Enter Tank 2 (Power):"))
tank2 = Tank(reloadRate, accuracy, armor, power)

drawTank("left", "green")
drawTank("right", "green")

moraleColor = ["red", "orange", "yellow", "green"]
moraleState = ["panicked", "scared", "worried", "calm"]
startTime = time.clock()
currentTime = time.clock()
tank1LastShot = time.clock()
tank2LastShot = time.clock()
tank1Wins = False
tank2Wins = False

while (not tank1Wins and not tank2Wins) or time.clock() - startTime > 100:
    currentTime = time.clock()
    if currentTime - tank1LastShot > tank1.reloadRate:
        #Tank 1 turn
        tank1LastShot = currentTime 
        if tank1.accuracy * tank1.morale > random.random():
            #Hit
            damage = (tank1.power - tank2.armor)//2
            tank2.health -= damage
            tank2.morale = max(tank2.morale - .25, .25)
            log("Tank 1 hit Tank 2 for " + str(damage))
            if tank2.health <= 0:
                tank1Wins = True
        else:
            tank2.morale = min(tank2.morale + .25, 1)
        
    
        drawTank("right", moraleColor[int (tank2.morale * 4 - 1)])

        log("tank1: " + moraleState[int (tank1.morale * 4 - 1)] + " tank2: " + moraleState[int (tank2.morale * 4 - 1)])

    if currentTime - tank2LastShot > tank2.reloadRate:
        #Tank 2 turn
        tank2LastShot = currentTime 
        if tank2.accuracy * tank2.morale > random.random():
            #Hit
            damage = (tank2.power - tank1.armor)//2
            tank2.health -= damage
            tank1.morale = max(tank1.morale - .25, .25)
            log("Tank 2 hit Tank 1 for " + str(damage))

            if tank1.health <= 0:
                tank2Wins = True
        else:
            tank1.morale = min(tank1.morale + .25, 1)
        
    
        drawTank("left", moraleColor[int (tank1.morale * 4 - 1)])

        log("tank2: " + moraleState[int (tank2.morale * 4 - 1)] + " tank1: " + moraleState[int (tank1.morale * 4 - 1)])

if tank1Wins == tank2Wins:
    log("Tie")
elif tank1Wins:
    log("Tank 1 Wins!")
elif tank2Wins:
    log("Tank 2 Wins!")
    


        
    




















