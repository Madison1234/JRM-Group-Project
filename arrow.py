import runWorld as rw
import drawWorld as dw
import pygame as pg

from random import randint

name = "Arrow Simulation"
width = 1100
height = 750
rw.newDisplay(width, height, name)


class State:
    x = 0
    y = 600
    v = 1


ballState = State()


myimage = dw.loadImage("soccer.jpeg")
goal=dw.loadImage("goall.gif")
player=dw.loadImage("p6.jpeg")
player2=dw.loadImage("p6.jpeg")

def updateDisplay(state):
    dw.fill(dw.green)
    dw.draw(myimage, (state.x, state.y))
    dw.draw(goal, (870,550))
    dw.draw(player,(0,500))
    dw.draw(player2, (550,10))

def updateState(state):
    if(state.x == 750 and state.v == 1):
        print("Goal!")
    state.x = state.x + state.v
    state.y = 0.003125*((state.x)**2)-(2.5*(state.x))+600
    state.v = state.v  
    return (state)

def endState(state):
    if (state.x > width or state.x < 0 or state.y > height or state.y < 0):
        return True
    else:
        return False

def handleEvent(state, event):
    if (event.type == pg.MOUSEBUTTONDOWN and state.x < 1000 and state.y < 750):
        return state
    elif (event.type == pg.KEYDOWN):
        state.v = state.v * -1
        return (state)
    else:
        return (state)
    

frameRate = 90

rw.runWorld(ballState, updateDisplay, updateState, handleEvent, endState, frameRate)
