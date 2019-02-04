## Name: Maaz Azam
## Student#: 400069421
## MacID: azamm3

from graphics import *

def distanceBetweenPoints(P1, P2):
    x1 = P1.getX() #get x-point of P1
    x2 = P2.getX() #get x-point of P2
    y1 = P1.getY() #get y-point of P1
    y2 = P2.getY() #get y-point of P2

    distance = ((x2-x1)**2+(y2-y1)**2)**0.5 #calculate distance
    return distance

def drawCircle(win,center,radius,color):
    c = Circle(center,radius) #draw circle of certain radius and center point
    c.setFill(color) #set colour scheme of circle
    c.draw(win) #draw circle on window
    return c

def main():
    win = GraphWin("Circle",540,400)
    center = Point(200,200)
    P1 = center
    radius = 50
    color = 'red'

    while True:
        c = drawCircle(win, center, radius, color)
        P2 = win.getMouse()
        distance = distanceBetweenPoints(P1,P2)
        c.undraw()
        if distance < radius:
            if distance < 0.25*radius:
                win.close()
            else:
                radius = 0.80*radius
        else:
            radius = radius*1.10
