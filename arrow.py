import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint

name = "Arrow Simulation"
width = 2000
height = 750
rw.newDisplay(width, height, name)

myimage = dw.loadImage("soccer.jpeg")
goal=dw.loadImage("goall.gif")
player=dw.loadImage("p6.jpeg")
player2=dw.loadImage("p6.jpeg")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state))
    dw.draw(goal, (870,550))
    dw.draw(player,(0,500))
    dw.draw(player2, (550,10))
    
    

def updateState(state):
    return(state[0] + 1, (0.003125*((state[0])**2))-(2.5*(state[0]))+600)

def endState(state):
    if (state[0] > width or state[0] < 0 or state[1] > height or state[1] < 0):
        return True
    else:
        return False

def handleEvent(state, event):
    if (event.type == pg.MOUSEBUTTONDOWN and state < (1000,750)):
        return initState
    else:
        return (state)

initState = (0, 600)

frameRate = 90

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)
